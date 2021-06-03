from engine.object_controllable import ControllableGameObject
from engine.interact import (HostileNpcExamine, FriendlyNpcExamine, Action,
                             ExamineResponse)


class Npc(ControllableGameObject):

    def __init__(self,
                 *args,
                 level: int = 0,
                 hostile: bool = False,
                 aggresive: bool = False,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.level = level
        self.hostile = hostile
        self.aggresive = aggresive
        self._examine = (HostileNpcExamine() if hostile
                         else FriendlyNpcExamine())

    def interract(self, action: Action) -> None:
        print(f'Interract with {self.name}')
        pass

    def examine(self) -> ExamineResponse:
        return self._examine
