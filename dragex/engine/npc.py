from engine.base_object import BaseObject
from engine.object_controller import ObjectController
from engine.animation import AnimationHandler
from engine.object_state import NpcState


class Combat:
    MELEE = 0
    RANGE = 1
    MAGIC = 2


class Npc(BaseObject):
    """ Base NPC object. """

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

        self.anim_handler = AnimationHandler(self)
        self.state: NpcState = NpcState(self.anim_handler)
        self.ctrl = ObjectController(self.position, self.state, speed)

        self.hp_max = hp_max
        self.hp = self.hp_max
        self.range = range
        self.combat_type = combat_type
        self.max_damage = max_damage
        self.damage_freq = damage_freq

    def set_state(self, state: NpcState) -> None:
        """ Changes the state of the npc. """
        self.state.set(state)

    def is_dead(self) -> bool:
        """ Returns if the npc is dead. """
        return self.hp <= 0

    def take_damage(self, damage: int) -> None:
        """ Reduces the npc's hitpoints by damage.
            The hp can't get below 0.
        """
        self.hp = min(0, self.hp-damage)

    def heal(self, hp: int) -> None:
        """ Increases the npc's hitpoints by hp.
            The hp can't exceed hp_max.
        """
        self.hp = min(self.hp_max, self.hp+hp)

    def draw(self, canvas) -> None:
        """ Draws the sprite of the npc to the canvas. """
        sprite = self.anim_handler.get_sprite()
        self.set_active_sprite(sprite)
        super().draw(canvas)

    def update(self, elapsed_time: float) -> None:
        """ Updates any state/physics of the npc. """
        self.ctrl.move(elapsed_time)
