from ui import basemodels
from utils import Levels


class Skill(basemodels.Frame):

    def __init__(self, master, name: str, xp: int):
        super().__init__(master)

        self._label_name = basemodels.Label(self, text=name)
        self._label_level = basemodels.Label(self)
        self._label_xp = basemodels.Label(self)

        self._label_name.pack()
        self._label_level.pack()
        self._label_xp.pack()

        self.update_stats(xp)

    def update_stats(self, xp: int) -> None:
        self._label_level.config(text=Levels.get_level(xp))
        self._label_xp.config(text=xp)
