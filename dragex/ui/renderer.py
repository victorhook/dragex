from engine import Controller
import tkinter as tk


class Renderer:

    def __init__(self, canvas: tk.Canvas):
        self.controller = Controller()
        self.canvas = canvas

    def render(self):
        for obj in self.controller.get_visible_objects():
            obj.draw(self.canvas)
