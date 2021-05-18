import tkinter as tk
import sys
from PIL import Image

from ui import styles
from ui.gamescreen import GameScreen
from ui.loginscreen import LoginScreen
from ui.uistate import UiState


class App(tk.Tk):

    WIDTH = 900
    HEIGHT = 700

    def __init__(self):
        super().__init__()
        self.title('Insane Game')
        self.config(bg=styles.frames['bg'])
        self.geometry(f'{App.WIDTH}x{App.HEIGHT}')

        self.state = UiState()
        self.game_screen = GameScreen(self)
        self.login_screen = LoginScreen(self)

        self.login_screen.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def login(self):
        pass

    def destroy(self):
        sys.exit(0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
