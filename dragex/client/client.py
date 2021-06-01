import threading

from client.base_client import Client


class DragexClient(Client):

    def init(self) -> None:
        self._flag = threading.Event()

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def login(self, username: str, password: str) -> bool:
        pass

    def logout(self) -> bool:
        pass

    def stop(self) -> None:
        self._flag.clear()

    def start(self) -> None:
        self._flag.set()
        self._running = True
        thread = threading.Thread(target=self._start)
        thread.start()

    def is_running(self) -> bool:
        return self._running

    def _start(self) -> None:
        while self._running and self._flag.is_set():
            self._communicate()

        print('Thread stopped!')
        self._running = False

    def _communicate(self) -> None:
        print('Running in background!')
