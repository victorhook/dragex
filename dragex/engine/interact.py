from typing import List
from dataclasses import dataclass


class Action:
    WALK = 0
    ATTACK = 1
    DIALOG = 2
    TRADE = 3
    INTERACT = 4


class Option:
    def __init__(self, title: str, action: int):
        self.title = title
        self.action = action

    def __repr__(self):
        return self.title


class OptionWalk(Option):
    def __init__(self):
        super().__init__('Walk here', Action.WALK)


class OptionDialog(Option):
    def __init__(self):
        super().__init__('Talk', Action.DIALOG)


class OptionAttack(Option):
    def __init__(self):
        super().__init__('Attack', Action.ATTACK)


class OptionTrade(Option):
    def __init__(self):
        super().__init__('Trade', Action.TRADE)


class OptionInteract(Option):
    def __init__(self):
        super().__init__('Interact', Action.INTERACT)


# --- Responses --- #

class ExamineResponse:

    def __init__(self, options: List[Option]):
        self.options = options

    def __repr__(self):
        return '\n'.join(str(opt) for opt in self.options)


class EmptyExamine(ExamineResponse):

    def __init__(self):
        super().__init__([OptionWalk()])


class PlayerExamine(ExamineResponse):

    def __init__(self):
        super().__init__([OptionWalk(), OptionAttack(), OptionTrade()])


class HostileNpcExamine(ExamineResponse):

    def __init__(self):
        super().__init__([OptionWalk(), OptionAttack()])


class FriendlyNpcExamine(ExamineResponse):

    def __init__(self):
        super().__init__([OptionWalk(), OptionDialog()])


class ObjectExamine(ExamineResponse):

    def __init__(self):
        super().__init__([OptionWalk(), OptionInteract()])
