import tkinter as tk
import io
import time
from PIL import Image, ImageTk

from engine import Controller
from . import basemodels
from .renderer import Renderer
from utils import Settings


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

    def __init__(self, master, width=800, height=800,
                 desired_fps=40):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height

        self._desired_fps = int(1000 * (1/(desired_fps)))

        self.canvas = tk.Canvas(self, width=width, height=height)
        self._buf = io.BytesIO()
        self._img = None
        self._tag = None
        self._tag = self.canvas.create_image(self.width/2, self.height/2,
                                             image=None)
        self._fps_lbl = self.canvas.create_text(20, 20, text='', font=('Courier', 20))
        self.canvas.pack()

        # Create renderer
        self.controller = Controller()
        self.renderer = Renderer(self.canvas)

        self._show_grids = True
        self.grids = None

        self.fps = Fps()

    def update_buffer(self, data: Image):
        self._buf = data

    def read_image(self) -> ImageTk.PhotoImage:
        return ImageTk.PhotoImage(self._buf)

    def render(self):
        self._update_fps()
        self.renderer.render()

        if self._show_grids:
            self._render_gridmap()

        self.after(self._desired_fps, self.render)

    def _render_gridmap(self):
        """ Renders the gridmap of the world to the screen.
            Useful for debugging.
        """
        if self.grids is None:
            grids = Settings.GRID_AMMOUNT
            gsize = Settings.GRID_SIZE

            self.grids = [[0 for i in range(grids)] for i in range(grids)]

            for r in range(grids):
                self.grids[r][0] = self.canvas.create_line(0, r*gsize, self.width, r*gsize)
                for c in range(grids):
                    self.grids[r][c] = self.canvas.create_line(c*gsize, 0, c*gsize, self.height)

    def _update_fps(self):
        self.fps.inc()
        self.canvas.itemconfigure(self._fps_lbl, text=self.fps.read())
