from utils import Singleton, AssetHandler
from objects import BaseObject
from factories.object_factory import ObjectFactory

from typing import List


class World:

    def __init__(self, world: dict = None):
        if world is not None:
            self.update(world)

    def update(self, world: dict):
        self.objects = List[BaseObject]
        #for obj in world:
        #    self.objects.append(ObjectFactory.create(obj))

    def __iter__(self) -> list:
        return self.objects


class RelativeWorld(World):
    pass


class AbsoluteWorld(World):
    pass


class WorldLoader(Singleton):

    @staticmethod
    def load() -> World:
        return World(AssetHandler.open_world())
