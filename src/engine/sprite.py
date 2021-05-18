import tkinter as tk
from PIL import ImageTk

from utils import AssetHandler, Position, Size


class Sprite:

    def __init__(self, position: Position, size: Size, source: str):
        self.position = position
        self.size = size
        self.source = source
        self.image = self._get_image()
        self._tag = None

    def draw(self, canvas: tk.Canvas):
        if self._tag is None:
            self._tag = self._create_image_tag(canvas)
        else:
            x, y = self._coords()
            canvas.coords(self._tag, x, y)

    def _get_image(self) -> ImageTk.PhotoImage:
        image = AssetHandler.open_asset(self.source)
        image = image.resize((self.size.width, self.size.height))
        return ImageTk.PhotoImage(image)

    def _coords(self) -> tuple:
        x = self.position.x / 2
        y = self.position.y / 2
        return x, y

    def _create_image_tag(self, canvas: tk.Canvas) -> str:
        x, y = self._coords()
        return canvas.create_image(x, y, image=self.image)
