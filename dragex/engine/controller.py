from typing import List

from client import DragexClient
from engine.world import WorldLoader
from engine.character import Character
from engine.event_queue import EventQueue
from factories.npc_factory import NpcFactory
from engine.sprite import SingleSprite
from engine.gridmap import GridMap
from engine.pathfinder import PathFinder
from objects import BaseObject
from engine.animation import Animation, AnimationHandler, Transition, SingleSpriteAnimation # noqa
from loaders.sprite_loader import SpriteLoader
from objects import ObjectState, Npc, Player
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

        self.character = Player('Nisse persson')
        self.game_objects = [self.character]

        #factory = NpcFactory()
        #goblin = NpcFactory.create('goblin')
        #self.game_objects.append(goblin)

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
        #self.character.active_sprite = SpriteLoader().get_sprite('man')
        self.character.anim_handler.add_animation('IDLE', Animation(frames=[Transition(self.LOADER.get_sprite('man'), .1)]))

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
