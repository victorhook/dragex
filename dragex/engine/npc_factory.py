from engine.npc import Npc
from engine.animation import Animation, Transition
from engine.sprite import Sprite, SingleSprite
from engine.object_state import ObjectState
import npcs
from utils import Singleton, AssetHandler

from pathlib import Path

from utils.size import Size


class NpcFactory(Singleton):

    _BASE_PATH = Path('npcs')

    def init(self) -> None:
        self._blueprint = AssetHandler.open_blueprints()

    def _get_npc_instance(self, npc: str) -> Npc:
        # First gets the module of the class.
        module = getattr(npcs, npc)
        # Then the concrete class, from the module.
        cls = getattr(module, npc.title())
        return cls()

    def _get_sprite(self, npc: Npc, sprite: str) -> Sprite:
        sprite_path = str(self._BASE_PATH.joinpath(npc.name.lower(), sprite))
        return SingleSprite(sprite_path, npc.size)

    def _set_skills(self, npc: Npc, skills: dict) -> None:
        for key, value in skills.items():
            setattr(npc, key, value)

    def _set_animation(self, npc: Npc, animations: dict) -> None:
        t_speed = animations['transition_speed']

        for int_state, str_state in ObjectState.STATE_STRINGS.items():
            transitions = []

            for sprite in animations[str_state]:
                sprite = self._get_sprite(npc, sprite)
                transitions.append(Transition(sprite, t_speed))

            npc.anim_handler.add_animation(int_state, 
                                           Animation(frames=transitions))

    def _set_size(self, npc: Npc, size: list) -> None:
        npc.size = Size(size[0], size[1])

    def create(self, npc: str) -> Npc:
        # Get the blueprint for this npc.
        blueprint = self._blueprint[npc]

        # Instantiate the new npc object.
        new_npc = self._get_npc_instance(npc)

        # Set correct size for the npc.
        self._set_size(new_npc, blueprint['size'])

        # Set appropiate skills.
        self._set_skills(new_npc, blueprint['stats'])

        # Set animations.
        self._set_animation(new_npc, blueprint['animations'])

        return new_npc
