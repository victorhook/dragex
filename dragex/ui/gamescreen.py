from collections import namedtuple
import tkinter as tk

from engine import Controller
from engine.event_queue import EventQueue, EventType
from ui import basemodels
from ui.examine import Examine
from ui.renderer import Renderer
from ui.chat import Chat
from ui.inventory import Inventory
from utils import Settings


class Cursor:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __call__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


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
        self.controller: Controller = Controller()
        self.event_queue: EventQueue = EventQueue()
        self.renderer: Renderer = Renderer(self.canvas)
        self._cursor: Cursor = Cursor()
        self._active_examine: Examine = None

        # Callbacks
        self.canvas.bind('<Motion>', self._motion)
        self.canvas.bind('<Button-1>', self._left_click)
        self.canvas.bind('<Button-3>', self._right_click)
        self.master.master.bind('<space>', self._space)

        self._char_state = self.canvas.create_text(100, 20, text='')

        self._show_grids = True
        self.grids = None

    def _motion(self, e):
        self._cursor(e.x, e.y)

    def _space(self, e) -> None:
        self.controller.space_bar(e)

    def _left_click(self, e) -> None:
        self.controller.left_button_press(e)

    def _right_click(self, e) -> None:
        self.controller.right_button_press(e)

    def _clear_old_examine(self) -> None:
        if self._active_examine is not None:
            self.canvas.delete(self._active_examine)

    def _handle_event_queue(self):
        event = self.event_queue.get()

        if event is not None:
            self._clear_old_examine()

            if event.event_type == EventType.STATUS_UPDATE:
                try:
                    text = event.payload.value
                except Exception:
                    text = 'Unknown error'
                self.canvas.itemconfigure(self._char_state, text=text)

            elif event.event_type == EventType.EXAMINE_RESPONSE:
                examine_popup = Examine(self, event.payload)
                x = self._cursor.x + examine_popup.width/2
                y = self._cursor.y + examine_popup.height/2

                self._active_examine = self.canvas.create_window(
                                                        x,
                                                        y,
                                                        window=examine_popup)

    def render(self, elapsed_time: float) -> None:
        self._handle_event_queue()

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
