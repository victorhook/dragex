from ui import basemodels


class ToolTip(basemodels.Frame):

    def __init__(self, master, text: str):
        super().__init__(master)
        self.text = basemodels.Label(self, text=text)
        self.text.pack()

        self._is_visible = False
        self.bind('<Leave>', self.leave)

    def leave(self, e):
        self._is_visible = False
        self.pack_forget()
