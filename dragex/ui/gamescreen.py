import tkinter as tk
import io
import time
from PIL import Image, ImageTk

from engine import Controller
from . import basemodels
from .renderer import Renderer
from utils import Settings


class GameScreen(basemodels.Frame):

    def __init__(self, master, width=800, height=800):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height

        self.canvas = tk.Canvas(self, width=width, height=height)
        self._buf = io.BytesIO()
        self._img = None
        self._tag = None
        self._tag = self.canvas.create_image(self.width/2, self.height/2,
                                             image=None)
        self.canvas.pack()

        # Create renderer
        self.controller = Controller()
        self.renderer = Renderer(self.canvas)

        # Callbacks
        self.canvas.bind('<Button-1>', self.controller.left_button_press)
        self.canvas.bind('<Button-3>', self.controller.right_button_press)

        self._show_grids = True
        self.grids = None

    def update_buffer(self, data: Image):
        self._buf = data

    def read_image(self) -> ImageTk.PhotoImage:
        return ImageTk.PhotoImage(self._buf)

    def render(self, elapsed_time: float) -> None:
        if self._show_grids:
            self._render_gridmap()

        self.renderer.render(elapsed_time)

    def _render_gridmap(self):
        """ Renders the gridmap of the world to the screen.
            Useful for debugging.
        """
        grids = Settings.GRID_AMMOUNT
        gsize = Settings.GRID_SIZE

        if self.grids is None:
            self.grids = [[0 for i in range(grids)] for i in range(grids)]

            for r in range(grids):
                for c in range(grids):
                    self.grids[r][c] = self.canvas.create_rectangle(c*gsize,
                    r*gsize,
                    c*gsize+gsize,
                    r*gsize+gsize,
                    fill='white')
        else:
            for r in range(grids):
                for c in range(grids):
                    self.canvas.itemconfigure(self.grids[r][c], fill='white')

        self.canvas.delete('path')