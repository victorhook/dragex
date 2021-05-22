from . import basemodels
from engine import Controller


class Toolbox(basemodels.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.control = Controller()

        self._btn_clear = basemodels.Button(self, text='Clear',
                                            command=self._clear)
        self._btn_add = basemodels.Button(self, text='Add character')
        self._btn_reset = basemodels.Button(self, text='Reset',
                                            command=self.control.reset)
        self._chk_obj = basemodels.CheckButton(self, text='Object')

        self._chk_obj.pack(side='left')
        self._btn_add.pack(side='left')
        self._btn_reset.pack(side='left')
        self._btn_clear.pack(side='left')


    def _clear(self):
        self.control.game_objects = [self.control.character]
        print(self.control.game_objects)

