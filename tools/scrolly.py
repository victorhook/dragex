from ui import basemodels
import tkinter as tk
from ui.scrollframe import ScrollableFrame


class Chat(basemodels.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.content = ScrollableFrame(self)

        self.bottom_frame = basemodels.Frame(self)
        self.input = basemodels.Entry(self.bottom_frame)
        self.btn_send = basemodels.Button(self.bottom_frame, text='Send',
                                          size=12, command=self._send)

        self.content.pack(fill=tk.X)
        self.btn_send.pack(side=tk.RIGHT)
        self.input.pack(side=tk.RIGHT, fill=tk.X)
        self.bottom_frame.pack(fill=tk.X)

    def _send(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()

    p = Chat(root)
    p.pack()

    root.mainloop()