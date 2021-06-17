import time
from typing import List

from objects import BaseObject
from utils import Singleton, Settings

from server.server import Server
from server.rng import Rng
from server.database import Database
from server.context import Context


class Event:
    pass


class Tickable(Singleton):

    def init(self):
        self.t0 = time.time()

    def _tick_time(self) -> bool:
        t1 = time.time()
        if t1 - self.t0 > Settings.TICK_DELAY_S:
            self.t0 = t1
            return True
        return False

    def tick(self) -> None:
        """ Performs a single game tick, if enough time
            has passed since the last tick.
        """
        if self._tick_time():
            self.game_tick()

    def game_tick(self) -> None:
        pass


class Engine(Tickable):

    def init(self,
             server: Server,
             game_objects: List[BaseObject] = [],
             events: List[Event] = [],
             rng: Rng = None,
             db: Database = None,
             ):

        super().init()

        self.server = Server
        self.game_objects = game_objects
        self.events = events
        self.rng = Rng() if rng is None else rng
        self.db = Database() if db is None else db

    def _time_to_save(self) -> bool:
        t1 = time.time()
        return t1 - self.t0 > Settings.DB_SAVE_DELAY

    def _get_context(self) -> Context:
        pass

    def _save(self) -> None:
        """ Saves the current game status to backend database. """
        context = self._get_context()
        self.db.save(context)

    def game_tick(self) -> None:
        if self._time_to_save():
            self._save()

        """
            - Calculate all loots that are needed.
            - Calculate all damages that should be taken.
            - Calculate all events that should occur? Death etc.
            - Spawn new monsters.
            - Check chats.
            - Broadcast events to all players.

            * Check private messages?

            loots = self.calculate_loots()
            damages = self.calculate_damages()
            events = self.calculate_events()
            new_monsters = self.spawn_new_monsters()
            chat_messages = self.get_chat_messages()
            private_messages = self.get_private_messages()
        """


        #self.server.broadcast(

        #)

    def serialize_game_objects(self):
        objects = []
        for game_object in self.game_objects:
            objects.append(game_object.serialize())
        return objects

    def calculate_loots(self):
        pass

    def calculate_damages(self):
        pass

    def calculate_events(self):
        pass

    def spawn_new_monsters(self):
        pass

    def get_chat_messages(self):
        pass

    def get_private_messages(self):
        pass
