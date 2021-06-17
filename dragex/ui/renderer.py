from engine import Controller
from interfaces.screen import Screen


class Renderer:

    def __init__(self, screen: Screen):
        self.controller = Controller()
        self.screen = screen

    def render(self, elapsed_time: float) -> None:
        for obj in self.controller.get_visible_objects():
            obj.update(elapsed_time)
            obj.draw(self.screen)
