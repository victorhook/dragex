from typing import List
from dataclasses import dataclass


class Action:
    ATTACK = 0
    DIALOG = 1
    TRADE = 2


class Option:
    title: str
    action: int


class OptionDialog(Option):
    def __init__():
        super().__init__('Talk', Action.DIALOG)


class OptionAttack(Option):
    def __init__():
        super().__init__('Attack', Action.ATTACK)


class OptionTrade(Option):
    def __init__():
        super().__init__('Trade', Action.TRADE)


@dataclass
class Response:
    options: List[Option]


class InteractResponse(Response):
    pass


class ExamineResponse(Response):
    pass