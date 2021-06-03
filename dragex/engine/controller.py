from typing import List

from client import DragexClient
from engine.character import Character
from engine.event_queue import EventQueue
from engine.sprite import SingleSprite
from engine.gridmap import GridMap
from engine.pathfinder import PathFinder
from engine.base_object import BaseObject, GridObject, WallObject
from engine.animation import Animation, AnimationHandler, Transition, SingleSpriteAnimation # noqa
from engine.object_state import ObjectState
from engine.npc import Npc
from engine.player import Player
import npcs
import utils
from utils import Singleton, Settings, Size


def is_player(obj: BaseObject) -> bool:
    return False


def is_enemy_npc(obj: BaseObject) -> bool:
    return isinstance(obj, Npc) and obj.hostile


def is_friendly_npc(obj: BaseObject) -> bool:
    return isinstance(obj, Npc) and not obj.hostile


class Controller(Singleton):

    def init(self):
        self.client = DragexClient()

        """
        self.character = Character('Hubert', 'Nisse', speed=5, world_x=10, world_y=10)

        sprite1 = SingleSprite(Size(1, 1), 'man.png')
        sprite2 = SingleSprite(Size(1, 1), 'man2.png')
        sprite3 = SingleSprite(Size(1, 1), 'man3.png')
        idle = SingleSpriteAnimation(sprite1)
        moving = Animation(frames=[Transition(sprite1, .1),
                                   Transition(sprite2, .1),
                                   Transition(sprite3, .1)])

        attack_sprite1 = SingleSprite(Size(1, 1), 'man_attack1.png')
        attack_sprite2 = SingleSprite(Size(1, 1), 'man_attack2.png')
        attacking = Animation(frames=[Transition(attack_sprite1, .1),
                                      Transition(attack_sprite2, .1)])

        self.character.anim_handler.add_animation(ObjectState.IDLE, idle)
        self.character.anim_handler.add_animation(ObjectState.MOVING, moving)
        self.character.anim_handler.add_animation(ObjectState.ATTACKING, attacking)
        """
        self.character = Player('Nisse persson')
        self.game_objects = [self.character]

        goblin = npcs.Goblin()
        goblin.ctrl.jump_to(utils.Grid(10, 12))
        self.game_objects.append(goblin)

        for i in range(8):
            self.game_objects.append(WallObject(world_x=8, world_y=2+i))
            self.game_objects.append(WallObject(world_x=12, world_y=2+i))

        self.event_queue = EventQueue()
        self.gridmap = GridMap()
        self.pathfinder = PathFinder()
        self.selected_object: BaseObject = None

    def reset(self):
        self.character.ctrl.curr_path = None
        self.character.ctrl.pos.x = 10
        self.character.ctrl.pos.y = 10
        self.character.ctrl.next_grid = 0
        self.character.ctrl.vel = (0, 0)

    def space_bar(self, event) -> None:
        grid = utils.get_grid(event.y, event.x)
        self.game_objects.append(WallObject(world_x=grid.col, world_y=grid.row-1))

    def right_button_press(self, key) -> None:
        target_grid = utils.get_grid(key.y, key.x)
        obj = self._get_clicked_object(target_grid)

        if obj is not None:
            response = obj.examine()
            self.event_queue.add(response)

        self.selected_object = obj

    def left_button_press(self, key) -> None:
        self.gridmap.fill(self.game_objects)
        target_grid = utils.get_grid(key.y, key.x)
        target_obj = self.gridmap[target_grid.row, target_grid.col]

        if self.gridmap.is_empty(target_grid):
            self.character.ctrl.set_target(target_grid)
        else:
            # Enemy
            if is_enemy_npc(target_obj):
                self.character.ctrl.attack_enemy(target_grid, target_obj)

            # Friendly npc
            elif is_friendly_npc(target_obj):
                pass

            # Skills
            else:
                pass

        # Better None type for clearing event queue?
        self.event_queue.add(None)

    def get_visible_objects(self) -> List[BaseObject]:
        """ Returns all game object that is visible. """
        drawables = list(filter(lambda obj: obj.is_visible(),
                                self.game_objects))
        return drawables

    def _get_clicked_object(self, grid: utils.Grid) -> BaseObject:
        for obj in self.game_objects:
            if obj.position.get_grid() == grid:
                return obj
        return None
