import tkinter as tk
import sys
from PIL import Image

from gamescreen import GameScreen


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Insane Game')

        self.screen = GameScreen(self)

        self.screen.pack()

        im = Image.open('assets/smiley.png')
        im = im.resize((800, 600))
        self.screen.update_buffer(im)

        self.screen.render()

    def destroy(self):
        sys.exit(0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
