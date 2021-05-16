import tkinter as tk
import basemodels
import io
import time
from PIL import Image, ImageTk


class Fps:

    def __init__(self):
        self.count = 0
        self._last_fps = 0
        self.t0 = time.time()

    def inc(self):
        self.count += 1

        t1 = time.time()
        if t1 - self.t0 > 1:
            self.t0 = t1
            self._last_fps = self.count
            self.count = 0

    def read(self):
        return self._last_fps


class GameScreen(basemodels.Frame):

    def __init__(self, master, width=800, height=600, fps=40):
        super().__init__(master)
        self._fps = int(1000 * (1/(fps)))
        self.master = master
        self.width = width
        self.height = height

        self.canvas = tk.Canvas(self, width=width, height=height)
        self._buf = io.BytesIO()
        self._img = None
        self._tag = None
        self._tag = self.canvas.create_image(self.width/2, self.height/2,
                                             image=None)
        self._fps_lbl = self.canvas.create_text(20, 20, text='', font=('Courier', 20))
        self.canvas.pack()

        self.fps = Fps()

    def update_buffer(self, data: Image):
        self._buf = data

    def read_image(self) -> ImageTk.PhotoImage:
        return ImageTk.PhotoImage(self._buf)

    def render(self):
        self.fps.inc()

        self._img = self.read_image()
        self.canvas.itemconfigure(self._tag, image=self._img)
        self.canvas.itemconfigure(self._fps_lbl, text=self.fps.read())

        self.after(self._fps, self.render)
