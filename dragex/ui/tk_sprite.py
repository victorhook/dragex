from PIL import Image, ImageTk

from engine.sprite import SingleSprite
from interfaces import Screen, SpriteImage
from utils import Position, Size


class TkSprite(SingleSprite):

    def __init__(self, name: str, size: Size, image: SpriteImage):
        super().__init__(name, size, image)
        self._tag = None
        self._raw_image = image

        # The name of the sprite is the same as the source name.
        self._set_image(self._raw_image)

    def do_draw(self, screen: Screen, x: int, y: int) -> None:
        if self._tag is None:
            self._tag = self._create_image_tag(screen, x, y)
        else:
            screen.coords(self._tag, x, y)
            if self._hidden:
                self.show(screen)

    def hide(self, screen: Screen) -> None:
        if self._tag:
            screen.itemconfigure(self._tag, state='hidden')
            self._hidden = True

    def show(self, screen: Screen) -> None:
        if self._tag:
            screen.itemconfigure(self._tag, state='normal')
            self._hidden = False

    def _create_image_tag(self, screen: Screen, x: int, y: int) -> str:
        return screen.create_image(x, y, image=self.image)

    def _set_image(self, image: Image) -> None:
        """ Sets the image to be displayed. """
        self.image = ImageTk.PhotoImage(image)
        self._tag = None

    def rotate(self, position: Position) -> None:
        angle = position.get_rotation_angle()
        image = self._raw_image.rotate(angle)
        self._set_image(image)

