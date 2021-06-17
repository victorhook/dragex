from objects import BaseObject
from objects import Player
from objects import Npc
from factories.npc_factory import NpcFactory
from npcs import Goblin
import utils


class ObjectFactory:

    __AVAILABLE_GAME_TYPES = None

    @staticmethod
    def get_available_game_objects() -> list:
        return [Player, Goblin]

    @staticmethod
    def serialize(obj: BaseObject) -> dict:
        """ Serializes a gameobject into a dictionary. """

        return {
            'type': obj.__class__.__name__,
            'name': obj.name,
            'description': obj.desription,
            'world_x': obj.position.x,
            'world_y': obj.position.y,
            'orientation': obj.position.orientation,
            'visible': obj.visible,
            'size': [obj.size.width, obj.size.height],
        }

    @staticmethod
    def create(obj: dict) -> BaseObject:
        """ Creates a game object from the given object dictionary. """
        ObjectClass = ObjectFactory._get_obj_class(obj['type'])

        if issubclass(ObjectClass, Npc):
            obj = NpcFactory.create(ObjectClass.__name__)
        else:
            obj = ObjectClass(
                name=obj['name'],
                description=obj['description'],
                world_x=obj['world_x'],
                world_y=obj['world_y'],
                orientation=obj['orientation'],
                visible=obj['visible'],
                size=obj['size']
            )

        return obj

    @staticmethod
    def _get_obj_class(obj_t: str) -> type:
        if ObjectFactory.__AVAILABLE_GAME_TYPES is None:
            ObjectFactory.__AVAILABLE_GAME_TYPES = ObjectFactory.get_available_game_objects() # noqa

        for obj_type in ObjectFactory.__AVAILABLE_GAME_TYPES:
            if obj_t.lower() == obj_type.__name__.lower():
                return obj_type
