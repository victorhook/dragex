from .character import Character
from .sprite import Sprite
from .gridmap import GridMap
from .pathfinder import PathFinder
from .base_object import GridObject, WallObject

from utils import Singleton, Settings
import utils


class Controller(Singleton):

    def __init__(self):
        self.character = Character('Hubert', world_x=10, world_y=10)
        self.character.visible = True
        self.character.active_sprite = Sprite(self.character.size, 'man.png')
        self.game_objects = [self.character]
        self.gridmap = GridMap()
        self.pathfinder = PathFinder()

    def right_button_press(self, key) -> None:
        target_grid = utils.get_grid(key.y, key.x)
        self.game_objects.append(WallObject(world_y=target_grid.row,
                                 world_x=target_grid.col))

    def left_button_press(self, key) -> None:
        target_grid = utils.get_grid(key.y, key.x)
        self.gridmap.fill(self.game_objects)

        nodes = self.pathfinder.find(self.gridmap, self.character.get_grid(),
                             target_grid)
        if nodes is None:
            return

        for node in nodes:
            self.game_objects.append(GridObject(node, world_y=node.row, world_x=node.col))

        return

        self.character.move(*target_grid)

    def get_visible_objects(self) -> list:
        """ Returns all game object that is visible. """
        drawables = list(filter(lambda obj: obj.is_visible(), self.game_objects))
        return drawables
