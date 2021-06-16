import unittest

from dragex.server.game_engine import Engine
from dragex.objects.environment import Environment
from dragex.engine.npc import Npc
from dragex.player import Player
from mock.server import MockServer


class TestSerialize(unittest.TestCase):

    def setUp(self):
        self.engine = Engine(
            MockServer()
        )

    def test_player(self):
        player = Player('CoolDude')
        self.engine.game_objects = [
            player
        ]
        serialized = self.engine.serialize_game_objects()
        self.assertEqual(player.serialize(), serialized[0])

    def test_npc(self):
        npc = Npc('Goblin')
        self.engine.game_objects = [
            npc
        ]
        serialized = self.engine.serialize_game_objects()
        self.assertEqual(npc.serialize(), serialized[0])

    def test_environment(self):
        env = Environment('Tree')
        self.engine.game_objects = [
            env
        ]
        serialized = self.engine.serialize_game_objects()
        self.assertEqual(env.serialize(), serialized[0])


unittest.main()