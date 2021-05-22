import tkinter as tk

from .base_object import BaseObject, GridObject
from .object_controller import ObjectController


class Character(BaseObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctrl = ObjectController(self.position)

    def draw(self, canvas: tk.Canvas) -> None:
        super().draw(canvas)
        if self.ctrl.next_grid:
            from utils import Settings
            y0 = self.ctrl.next_grid.row * Settings.GRID_SIZE
            x0 = self.ctrl.next_grid.col * Settings.GRID_SIZE
            canvas.create_rectangle(x0, y0, x0+Settings.GRID_SIZE,
                                     y0+Settings.GRID_SIZE, fill='red',
                                     tag='path')

    def update(self, elapsed_time: float) -> None:
        self.ctrl.move(elapsed_time)
