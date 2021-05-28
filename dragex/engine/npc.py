from engine.object_controllable import ControllableGameObject
from engine import interact


class Npc(ControllableGameObject):

    def __init__(self, *args, hostile: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.hostile = hostile
        if self.hostile:
            self._examine = interact.HostileNpcExamine()
        else:
            self._examine = interact.FriendlyNpcExamine()

    def interract(self, action: interact.Action) -> None:
        print(f'Interract with {self.name}')
        pass

    def examine(self) -> interact.ExamineResponse:
        return self._examine
