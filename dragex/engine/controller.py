from .character import Character
from .sprite import Sprite
from utils import Singleton
from utils import Settings


class Controller(Singleton):

    def __init__(self):
        character = Character('Hubert')
        character.visible = True
        character.active_sprite = Sprite(character.size, 'man.png')
        self.game_objects = [character]

    def get_visible_objects(self) -> list:
        """ Returns all game object that is visible. """
        drawables = list(filter(lambda obj: obj.visible, self.game_objects))
        return drawables
