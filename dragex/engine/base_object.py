from typing import List

import utils
from engine.drawable import Drawable
from engine.interact import ExamineResponse, Action
from engine.sprite import Sprite
from engine.serialize import Serializable
from engine.screen import Screen
from utils import Size, Position


class BaseObject(Drawable, Serializable):

    _obj_id = 0

    def __init__(self,
                 name: str = None,
                 desription: str = None,
                 world_x: int = 0,
                 world_y: int = 0,
                 orientation: int = 0,
                 visible: bool = True,
                 size: Size = None,
                 active_sprite: Sprite = None,
                 ):
        self.id = BaseObject._obj_id
        BaseObject._obj_id += 1

        self.name = self._get_name(name)
        self.desription = desription
        self.position = Position(world_x, world_y, orientation)
        self.size = self._get_size(size)
        self.visible = visible
        self.active_sprite = active_sprite
        self._last_sprite = active_sprite

    def get_grids(self) -> List[utils.Grid]:
        grids = set()
        if self.size.width == 1 and self.size.height == 1:
            grids.add(utils.Grid(self.position.y, self.position.x))
        else:
            for row in range(self.size.height):
                for col in range(self.size.width):
                    y = self.position.y + row
                    x = self.position.x + col
                    grids.add(utils.Grid(y, x))

        return grids

    def is_visible(self):
        return self.visible

    def set_active_sprite(self, sprite: Sprite) -> None:
        self.active_sprite = sprite

    def draw(self, screen: Screen) -> None:
        if not self.visible:
            # TODO : Remove this, debug only.
            print('Not visible, not drawing')
            return

        self.active_sprite.draw(self.position, screen)

        if (self.active_sprite is not self._last_sprite
           and self._last_sprite is not None):
            # Hide old sprite.
            self._last_sprite.hide(screen)
            pass

        self._last_sprite = self.active_sprite

    def serialize(self):
        return {
            'id': self.id,
            'object_type': self.__class__.__name__,
            'name': self.name,
            'world_y': self.position.y,
            'world_x': self.position.x,
            'orientation': self.position.orientation,
        }

    def interract(self, action: Action) -> None:
        """ Interracts with the object.
        """
        pass

    def examine(self) -> ExamineResponse:
        """ Examines the object.
            Returns an ExamineResponse, which the invoker
            can use.
        """

    def __str__(self):
        return self.name

    def __eq__(self):
        return self.id

    def _get_name(self, name: str) -> str:
        if name is None:
            # Create new default name.
            name = f'Object {BaseObject._obj_id}'
            BaseObject._obj_id += 1

        return name

    def _get_size(self, size: Size) -> Size:
        if size is None:
            size = Size(1, 1)
        return size
