from engine import interact
from ui import basemodels


class ExamineOption(basemodels.Label):

    def __init__(self, master, text: str, action: int):
        super().__init__(master, text=text)
        self._action = action
        self.bind('<Button-1>', lambda e: print(text))


class Examine(basemodels.Frame):

    def __init__(self, master, response: interact.ExamineResponse):
        super().__init__(master)
        options = []
        width = 0
        height = 0
        for option in response.options:
            opt = ExamineOption(self, option.title, option.action)
            opt.pack(anchor='w')
            options.append(opt)

            # Update frame dimensions.
            width = max(width, opt.winfo_reqwidth())
            height += opt.winfo_reqheight()

        self.configure(width=width, height=height)
        self.pack_propagate(0)
        self.width = width
        self.height = height