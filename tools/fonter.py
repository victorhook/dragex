import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

from engine.base_object import BaseObject
from engine.sprite import Sprite


BASE = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.join(BASE, 'assets')


def get_image(asset: str) -> bytes:
    return Image.open(os.path.join(BASE, asset))


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Insane Game')

        self.c = tk.Canvas(self, width=400, height=400)

        self.obj = BaseObject(rel_x=100, rel_y=100, size=(32, 32))
        self.sprite = Sprite(self.obj.pos_relative, self.obj.size, 'man.png')
        self.sprite.draw(self.c)

        self.c.pack()

    def login(self):
        pass

    def destroy(self):
        sys.exit(0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
