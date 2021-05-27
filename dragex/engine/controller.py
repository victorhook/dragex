from typing import List

from engine.character import Character
from engine.sprite import Sprite
from engine.gridmap import GridMap
from engine.pathfinder import PathFinder
from engine.base_object import BaseObject, GridObject, WallObject
from engine.animation import Animation, AnimationHandler, Transition, SingleSpriteAnimation # noqa
from engine.object_state import NpcState

import npcs
from utils import Singleton, Settings, Size
import utils



class Controller(Singleton):

    def init(self):
        self.character = Character('Hubert', 'Nisse', speed=5, world_x=10, world_y=10)

        sprite1 = Sprite(Size(1, 1), 'man.png')
        sprite2 = Sprite(Size(1, 1), 'man2.png')
        idle = SingleSpriteAnimation(sprite1)
        moving = Animation(frames=[Transition(sprite1, .1),
                                   Transition(sprite2, .1)])

        self.character.anim_handler.add_animation(NpcState.IDLE, moving)
        self.character.anim_handler.add_animation(NpcState.MOVING, moving)
        #self.character.anim_handler.add_animation(NpcState.MOVING, moving)

        self.game_objects = [self.character]

        goblin = npcs.Goblin()
        goblin.ctrl.jump_to(utils.Grid(10, 12))
        self.game_objects.append(goblin)

        for i in range(8):
            self.game_objects.append(WallObject(world_x=8, world_y=2+i))
            self.game_objects.append(WallObject(world_x=12, world_y=2+i))

        self.gridmap = GridMap()
        self.pathfinder = PathFinder()

    def reset(self):
        self.character.ctrl.curr_path = None
        self.character.ctrl.pos.x = 10
        self.character.ctrl.pos.y = 10
        self.character.ctrl.next_grid = 0
        self.character.ctrl.vel = (0, 0)

    def right_button_press(self, key) -> None:
        target_grid = utils.get_grid(key.y, key.x)
        self.game_objects.append(WallObject(world_y=target_grid.row,
                                 world_x=target_grid.col))

    def left_button_press(self, key) -> None:
        self.gridmap.fill(self.game_objects)
        target_grid = utils.get_grid(key.y, key.x)
        self.character.ctrl.set_target(target_grid)

    def get_visible_objects(self) -> List[BaseObject]:
        """ Returns all game object that is visible. """
        drawables = list(filter(lambda obj: obj.is_visible(),
                                self.game_objects))
        return drawables
