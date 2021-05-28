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
        for option in response.options:
            opt = ExamineOption(self, option.title, option.action)
            opt.pack()
            options.append(opt)

        opt = ExamineOption(self, 'asdasd', option.action)
        opt.pack()
        options.append(opt)
