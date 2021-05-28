from queue import Queue
from engine.interact import ExamineResponse

from utils import Singleton


class EventType:

    EXAMINE_RESPONSE = 1


def _get_event_type(event: object):
    if isinstance(event, ExamineResponse):
        return EventType.EXAMINE_RESPONSE
    return 0


class Event:

    def __init__(self, event_type: int, payload: object):
        self.event_type = event_type
        self.payload = payload


class EventQueue(Singleton):

    def init(self):
        self._queue = Queue()

    def add(self, event: object) -> None:
        """ Adds the event to the event queue. """
        event_t = _get_event_type(event)
        self._queue.put(Event(event_t, event))

    def get(self) -> Event:
        """ Returns the next event in the queue.
            Returns None if the queue is empty.
        """
        if len(self) > 0:
            return self._queue.get()
        return None

    def __len__(self):
        return len(self._queue.queue)
