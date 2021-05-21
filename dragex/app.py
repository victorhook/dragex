import tkinter as tk
import sys
from PIL import Image, ImageTk

from engine import Controller

from ui import styles
from ui.gamescreen import GameScreen
from ui.loginscreen import LoginScreen
from ui.uistate import UiState
from ui.toolbox import Toolbox
from ui import basemodels
from utils import AssetHandler, Fps


class App(tk.Tk):

    WIDTH = 900
    HEIGHT = 800

    def __init__(self):
        super().__init__()
        self.set_configs()

        self.state = self.start_state()
        self.frame = basemodels.Frame(self)

        self.game_screen = GameScreen(self.frame)
        self.login_screen = LoginScreen(self.frame)
        self.active_screen = self.update_active_screen()

        self.tools = Toolbox(self)
        self.tools.pack()

        self.frame.pack()

        # FPS
        self.fps = Fps()
        desired_fps = 30
        self._desired_fps = int(1000 * (1/(desired_fps)))
        self._fps_lbl = basemodels.Label(self)
        self._fps_lbl.pack()

        self.controller = Controller()
        self.controller.gridmap

        self.render()

    def start_state(self):
        return UiState.GAME

    def update_active_screen(self):
        if self.state == UiState.LOGIN:
            self.game_screen.pack_forget()
            self.login_screen.pack()
            self.active_screen = self.game_screen
        elif self.state == UiState.GAME:
            self.login_screen.pack_forget()
            self.game_screen.pack()
            self.active_screen = self.game_screen
        return self.active_screen

    def render(self):
        self.fps.inc()
        self._fps_lbl.config(text=self.fps.read())

        self.active_screen.render()

        self.after(self._desired_fps, self.render)

    def login(self):
        pass

    def destroy(self):
        sys.exit(0)

    def set_configs(self):
        self.title('Dragex')
        self.logo = ImageTk.PhotoImage(AssetHandler.open_image('logo.png'))
        self.iconphoto(False, self.logo)
        self.config(bg=styles.frames['bg'])
        #self.geometry(f'{App.WIDTH}x{App.HEIGHT}')


if __name__ == '__main__':
    app = App()
    app.mainloop()
