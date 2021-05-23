from ui import basemodels
import tkinter as tk


class Healthbar(tk.Canvas):

    def __init__(self, master, max: int):
        self.width = 100
        self.height = 30
        self.max = max
        super().__init__(master, width=self.width, height=self.height)

        self.outer = self.create_rectangle(0, 0, self.width, self.height,
                                           outline='black', width=2)
        self.green = self.create_rectangle(0, 0, self.width, self.height,
                                           fill='#ddd333')
        self.red = self.create_rectangle(0, 0, 0, 0, fill='red')
        self.text = self.create_text(self.width/2, self.height/2,
                                     font=('Courier', 18), fill='black')

    def update(self, hp: int):
        perc = hp / self.max
        text = f'{hp}/{self.max}'
        red = perc * self.width
        green = self.width - red

        self.itemconfigure(self.text, text=text)
        self.coords(self.red, red, 0, self.width, self.height)
        self.coords(self.green, 0, 0, green, self.height)

