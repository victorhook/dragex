import tkinter as tk
from PIL import ImageTk
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


def _game_position_to_pixel_coords(position: Position) -> Coordinates:
    """ Turns game position, aka grid square position into
        pixel coordinates.
        Returns a tuple of (x, y).
    """
    x = position.x * Settings.GRID_SIZE + (Settings.GRID_SIZE / 2)
    y = position.y * Settings.GRID_SIZE + (Settings.GRID_SIZE / 2)
    return Coordinates(x, y)


def _get_image(source: str, width: int, height: int) -> ImageTk.PhotoImage:
    image = AssetHandler.open_sprite(source)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)


class Sprite:

    def __init__(self, size: Size, source: str):
        self.size = _game_size_to_pixel_dimenions(size)
        self.source = source
        self.image = _get_image(source, self.size.width, self.size.height)
        self._tag = None
        self._hidden = False
        self._orientation: Orientation = None

    def draw(self, position: Position, canvas: tk.Canvas):
        x, y = _game_position_to_pixel_coords(position)

        if (self._orientation is None
           or position.orientation != self._orientation):
            self._orientation = position.orientation
            self._rotate_image()

        elif self._tag is None:
            self._tag = self._create_image_tag(canvas, x, y)
        else:
            canvas.coords(self._tag, x, y)
            if self._hidden:
                self.show(canvas)

    def _rotate_image(self) -> None:
        #self._orientation
        pass

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


class NullSprite(Sprite):

    def __init__(self):
        super().__init__(Size(1, 1), 'null.png')
