from objects import Npc
from engine.animation import Animation, Transition
from engine.sprite import Sprite, SingleSprite
from objects import ObjectState
from loaders.sprite_loader import SpriteLoader
import npcs
from utils import Singleton, AssetHandler

from pathlib import Path

from utils.size import Size


class NpcFactory:

    __BASE_PATH = Path('npcs')
    __BLUEPRINTS = None

    def _get_npc_instance(npc: str) -> Npc:
        # Retrieve the npc class from the "npcs" module.
        Class = getattr(npcs, npc.title())
        return Class()

    def _get_sprite(npc: Npc, sprite: str) -> Sprite:
        """
            Sprite path name for npcs are:
            npcs.NpcName.SpriteName
        """
        sprite_path = str(NpcFactory.__BASE_PATH.joinpath(npc.name.lower(),
                                                          sprite))
        return SpriteLoader.instance().get_sprite(sprite_path, npc.size)

    def _set_skills(npc: Npc, skills: dict) -> None:
        for key, value in skills.items():
            setattr(npc, key, value)

    def _set_animation(npc: Npc, animations: dict) -> None:
        t_speed = animations['transition_speed']

        for int_state, str_state in ObjectState.STATE_STRINGS.items():
            transitions = []

            for sprite in animations[str_state]:
                sprite = NpcFactory._get_sprite(npc, sprite)
                transitions.append(Transition(sprite, t_speed))

            npc.anim_handler.add_animation(int_state,
                                           Animation(frames=transitions))

    def _set_size(npc: Npc, size: list) -> None:
        npc.size = Size(size[0], size[1])

    def _get_blueprint(npc: str) -> dict:
        if NpcFactory.__BLUEPRINTS is None:
            NpcFactory.__BLUEPRINTS = AssetHandler.open_blueprint('npcs')
        return NpcFactory.__BLUEPRINTS[npc.title()]

    def create(npc: str) -> Npc:
        # Get the blueprint for this npc.
        blueprint = NpcFactory._get_blueprint(npc)

        # Instantiate the new npc object.
        new_npc = NpcFactory._get_npc_instance(npc)

        # Set correct size for the npc.
        NpcFactory._set_size(new_npc, blueprint['size'])

        # Set appropiate skills.
        NpcFactory._set_skills(new_npc, blueprint['stats'])

        # Set animations.
        NpcFactory._set_animation(new_npc, blueprint['animations'])

        return new_npc
