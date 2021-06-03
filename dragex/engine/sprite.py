import tkinter as tk
from typing import List
from PIL import ImageTk, Image
from collections import namedtuple

from utils import AssetHandler, Size, Position
from utils.position import Orientation
from .drawable import Drawable
from utils import Settings


Dimension = namedtuple('Dimension', ['width', 'height'])
Coordinates = namedtuple('Coordinates', ['x', 'y'])


def _game_size_to_pixel_dimenions(size: Size) -> Dimension:
    """ Turns a game size into pixel dimensions.
        Returns a tuple of (width, height).
    """
    width = size.width * Settings.GRID_SIZE
    height = size.height * Settings.GRID_SIZE
    return Dimension(width, height)


def _game_position_to_pixel_coords(size: Size,
                                   position: Position) -> Coordinates:
    """ Turns game position, aka grid square position into
        pixel coordinates.
        Returns a tuple of (x, y).
    """
    x = position.x * Settings.GRID_SIZE + size.width*(Settings.GRID_SIZE / 2)
    y = position.y * Settings.GRID_SIZE + size.height*(Settings.GRID_SIZE / 2)

    return Coordinates(x, y)


def _get_image(source: str, size: Size) -> Image:
    if not source.endswith(Settings.SPRITE_EXTENSION):
        source += Settings.SPRITE_EXTENSION

    pixel_size = _game_size_to_pixel_dimenions(size)
    image = AssetHandler.open_sprite(source)
    image = image.resize((pixel_size.width, pixel_size.height))
    return image


class Sprite:

    def draw(self, position: Position, canvas: tk.Canvas):
        pass

    def hide(self, canvas: tk.Canvas) -> None:
        pass

    def show(self, canvas: tk.Canvas) -> None:
        pass


class SingleSprite(Sprite):

    def __init__(self, source: str, size: Size = Size(1, 1)):
        self.source = source
        self.size = size
        
        self._tag = None
        self._hidden = False
        self._orientation: Orientation = None

        self._raw_image = _get_image(source, size)
        self._set_image(self._raw_image)

    def _set_image(self, image: Image) -> None:
        """ Sets the image to be displayed. """
        self.image = ImageTk.PhotoImage(image)
        self._tag = None

    def _rotate(self, position: Position) -> None:
        angle = position.get_rotation_angle()
        image = self._raw_image.rotate(angle)
        self._set_image(image)

    def draw(self, position: Position, canvas: tk.Canvas):
        x, y = _game_position_to_pixel_coords(self.size, position)

        if (self._orientation is None
           or position.orientation != self._orientation):
            self._orientation = position.orientation
            self._rotate(position)

        if self._tag is None:
            self._tag = self._create_image_tag(canvas, x, y)
        else:
            canvas.coords(self._tag, x, y)
            if self._hidden:
                self.show(canvas)

    def hide(self, canvas: tk.Canvas) -> None:
        if self._tag:
            canvas.itemconfigure(self._tag, state='hidden')
            self._hidden = True

    def show(self, canvas: tk.Canvas) -> None:
        if self._tag:
            canvas.itemconfigure(self._tag, state='normal')
            self._hidden = False

    def _create_image_tag(self, canvas: tk.Canvas, x: int, y: int) -> str:
        return canvas.create_image(x, y, image=self.image)


class NullSprite(SingleSprite):

    def __init__(self):
        super().__init__(Size(1, 1), 'null.png')


class EmptySprite(Sprite):
    pass


class SpriteCollection(Sprite):
    """ This class holds several Sprites and lets us
        use treat them as a single sprite.
    """
    def __init__(self):
        self._sprites: List[Sprite] = []

    def add(self, sprite: Sprite) -> None:
        self._sprites.append(sprite)

    def __iter__(self) -> list:
        return self._sprites

    def draw(self, position: Position, canvas: tk.Canvas) -> None:
        for sprite in self._sprites:
            sprite.draw(position, canvas)

    def hide(self, canvas: tk.Canvas) -> None:
        for sprite in self._sprites:
            sprite.hide(canvas)

    def show(self, canvas: tk.Canvas) -> None:
        for sprite in self._sprites:
            sprite.show(canvas)
