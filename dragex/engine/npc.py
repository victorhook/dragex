from engine.base_object import BaseObject
from engine.object_controller import ObjectController
from engine.animation import AnimationHandler
from engine.sprite import Sprite


class Combat:
    MELEE = 0
    RANGE = 0
    MAGIC = 0


class Npc(BaseObject):

    def __init__(self,
                 name: str,
                 description: str,
                 speed: int = 1,
                 hp_max: int = 10,
                 range: int = 1,
                 combat_type: int = Combat.MELEE,
                 max_damage: int = 1,
                 damage_freq: float = 0.3,
                 **kwargs
                 ):
        super().__init__(name, description, **kwargs)
        self.ctrl = ObjectController(self.position, speed)
        self.anim_handler = AnimationHandler(self)

        self.hp_max = hp_max
        self.hp = self.hp_max
        self.range = range
        self.combat_type = combat_type
        self.max_damage = max_damage
        self.damage_freq = damage_freq

    def is_dead(self) -> bool:
        return self.hp <= 0

    def take_damage(self, damage: int) -> None:
        self.hp = min(0, self.hp-damage)

    def heal(self, hp: int) -> None:
        self.hp = min(self.hp_max, self.hp+hp)

    def draw(self, canvas) -> None:
        sprite = self.anim_handler.get_sprite()
        self.set_active_sprite(sprite)
        print(sprite)
        super().draw(canvas)

    def update(self, elapsed_time: float) -> None:
        self.ctrl.move(elapsed_time)
