from typing import List

from interfaces import Screen, SpriteImage
from utils import Size, Position, image as image_utils
from utils.position import Orientation


class Sprite:

    """ Sprite interface. """

    def draw(self, position: Position, screen: Screen) -> None:
        pass

    def hide(self, screen: Screen) -> None:
        pass

    def show(self, screen: Screen) -> None:
        pass


class SingleSprite(Sprite):

    """ Abstract Single Sprite class.
        This class implements a single sprite while being
        agnostic of the low level image handling library.
    """

    _id = 0

    def __init__(self, name: str, size: Size, image: SpriteImage):
        # Set name & size and increment id.
        self.name = name
        self.size = size
        self.image = image

        self._hidden = False
        self._orientation: Orientation = None

        self.id = SingleSprite._id
        SingleSprite._id += 1

    def draw(self, position: Position, screen: Screen) -> None:
        x, y = image_utils._game_position_to_pixel_coords(self.size, position)

        if (self._orientation is None
           or position.orientation != self._orientation):
            self._orientation = position.orientation
            self.rotate(position)

        self.do_draw(screen, x, y)

    def do_draw(self, screen: Screen, x: int, y: int) -> None:
        """ Draws the actual sprite to the screen. """
        pass

    def hide(self, screen: Screen) -> None:
        """ Hides the sprite from the screen. """
        pass

    def show(self, screen: Screen) -> None:
        pass

    def rotate(self, position: Position) -> None:
        pass


class SpriteCollection(Sprite):

    """ This class holds several Sprites and lets us
        use treat them as a single sprite.
    """

    def __init__(self):
        self._sprites: List[Sprite] = []

    def add(self, sprite: Sprite) -> None:
        self._sprites.append(sprite)

    def draw(self, position: Position, screen: Screen) -> None:
        for sprite in self._sprites:
            sprite.draw(position, screen)

    def hide(self, screen: Screen) -> None:
        for sprite in self._sprites:
            sprite.hide(screen)

    def show(self, screen: Screen) -> None:
        for sprite in self._sprites:
            sprite.show(screen)

    def __iter__(self) -> list:
        return self._sprites


class NullSprite(Sprite):
    pass
