import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

from engine.base_object import BaseObject
from engine.sprite import Sprite
from utils import AssetHandler


BASE = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.join(BASE, 'assets')


def get_image(asset: str) -> bytes:
    return Image.open(os.path.join(BASE, asset))


class ToolTip(tk.Frame):

    def __init__(self, master, text: str):
        super().__init__(master)
        self.text = tk.Label(self, text=text)
        self.text.pack()

        self._is_visible = False
        self.bind('<Leave>', self.leave)

    def leave(self, e):
        self._is_visible = False
        self.pack_forget()


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Dragex')
        self.logo = ImageTk.PhotoImage(AssetHandler.open_image('logo.png'))
        self.iconphoto(False, self.logo)

        tooltip = ToolTip(self, 'This is a tooltip')

        self.l = tk.Label(self, text='Hello World!')
        self.l.bind('<Enter>', lambda k: tooltip.pack())
        self.l.pack()


    def login(self):
        pass

    def destroy(self):
        sys.exit(0)


if __name__ == '__main__':
    app = App()
    from tkinter import font

    app.mainloop()
