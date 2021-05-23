from ui import basemodels
from ui.scrollframe import ScrollableFrame
import tkinter as tk


class Chat(basemodels.Frame):

    def __init__(self, master, width):
        super().__init__(master)

        self.content = ScrollableFrame(self, width=width)
        self.bottom_frame = basemodels.Frame(self)
        self.input = basemodels.Entry(self.bottom_frame, size=16)
        self.btn_send = basemodels.Button(self.bottom_frame, text='Send',
                                          size=12, no_pad=True,
                                          command=self._send)

        self.content.pack(fill=tk.X)
        self.btn_send.pack(side=tk.RIGHT)
        self.input.pack(fill=tk.X, pady=10)
        self.bottom_frame.pack(fill=tk.X)

        for i in range(20):
            t = tk.Label(self.content(), text=str(i))
            t.pack()

    def _send(self):
        pass
