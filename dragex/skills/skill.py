from dataclasses import dataclass
from typing import List

from utils.levels import Levels


SKILLS = [
    'Hitpoints',
    'Strength',
    'Archery',
    'Magic',
    'Healing',
    'Speed',
    'Stamina',
    'Woodcutting',
    'Mining',
    'Fishing',
    'Cooking',
    'Crafting',
]


@dataclass
class Ability:
    name: str
    description: str
    level: int


@dataclass
class Skill:
    name: str
    experience: int
    abilities: List[Ability]

    def get_level(self) -> int:
        return Levels.get_level(self.experience)
