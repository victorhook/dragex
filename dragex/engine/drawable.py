import tkinter as tk


class Drawable:

    def update(self, elapsed_time: float) -> None:
        """ Updates any state that the object has. """
        pass

    def draw(self, canvas: tk.Canvas) -> None:
        """ Draws somethings on the canvas. """
        pass
