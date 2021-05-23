from ui import basemodels
from ui.healthbar import Healthbar
from ui.skill import Skill


class Slot(basemodels.Frame):

    def __init__(self, master):
        super().__init__(master, relief='ridge', width=40)
        self.item = basemodels.Label(self, bitmap='question')
        self.item.pack()


class Inventory(basemodels.LabelFrame):

    def __init__(self, master, width: int):
        super().__init__(master, text='Inventory', fg='white', width=width)

        size = 5
        self.slots = [[0 for i in range(size)] for i in range(size)]

        for row in range(size):
            for col in range(size):
                slot = Slot(self)
                self.slots[row][col] = slot
                slot.grid(row=row, column=col, padx=2, pady=2)

