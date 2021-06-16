from ui import basemodels
import tkinter as tk


class ScrollableFrame(basemodels.Frame):
    """ Wrapper class that allows a frame to be scrollable. """

    def __init__(self, master, width, **kwargs):
        super().__init__(master, **kwargs)

        self._canvas = tk.Canvas(self, height=100, width=width)
        self._scroll = basemodels.Scrollbar(self, orient='vertical',
                                            command=self._canvas.yview)

        self._scrollable_frame = basemodels.Frame(self._canvas)
        self._scrollable_frame.bind('<Configure>',
                                    lambda e: self._canvas.configure(
                                        scrollregion=self._canvas.bbox('all'))
                                    )

        self._canvas.create_window((0, 0), window=self._scrollable_frame,
                                   anchor='nw')
        self._canvas.configure(yscrollcommand=self._scroll.set)

        self._canvas.pack(side="left", fill="both", expand=True)
        self._scroll.pack(side="right", fill="y")

    def __call__(self) -> tk.Frame:
        return self._scrollable_frame

    def frame(self) -> tk.Frame:
        return self._scrollable_frame

