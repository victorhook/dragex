from engine import Controller
import tkinter as tk


class Renderer:

    def __init__(self, canvas: tk.Canvas):
        self.controller = Controller()
        self.canvas = canvas

    def render(self, elapsed_time: float) -> None:
        for obj in self.controller.get_visible_objects():
            obj.update(elapsed_time)
            obj.draw(self.canvas)
