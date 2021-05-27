import tkinter as tk
import io
import time
from PIL import Image, ImageTk

from engine import Controller
from . import basemodels
from .renderer import Renderer
from .chat import Chat
from .inventory import Inventory
from utils import Settings


class GameScreen(basemodels.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.width = Settings.GRID_SIZE * Settings.GRID_AMMOUNT
        self.height = Settings.GRID_SIZE * Settings.GRID_AMMOUNT

        inventory_width = 200

        # Frame for inventory and game canvas
        self.frame = basemodels.Frame(self)
        self.canvas = tk.Canvas(self.frame, width=self.width,
                                height=self.height)
        self.chat = Chat(self.frame, width=self.width)

        self.canvas.pack()
        self.chat.pack(fill=tk.X)

        self.inventory = Inventory(self, width=inventory_width)

        self.frame.pack(side='left')
        self.inventory.pack(side='right')

        # Create renderer
        self.controller = Controller()
        self.renderer = Renderer(self.canvas)

        # Callbacks
        self.canvas.bind('<Motion>', self._motion)
        self.canvas.bind('<Button-1>', self.controller.left_button_press)
        self.canvas.bind('<Button-3>', self.controller.right_button_press)

        self._show_grids = True
        self.grids = None

    def _motion(self, e):
        #print(self.canvas.find_overlapping(e.x, e.y, e.x, e.y))
        pass

    def render(self, elapsed_time: float) -> None:

        if self._show_grids:
            #self._render_gridmap()
            pass

        self.renderer.render(elapsed_time)
        self.canvas.update_idletasks()


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