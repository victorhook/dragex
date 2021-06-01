from utils import Singleton


class Client(Singleton):

    def connect(self) -> None:
        """ Connects to the backend dragex server. """
        pass

    def disconnect(self) -> None:
        """ Disconnects to the backend dragex server. """
        pass

    def login(self, username: str, password: str) -> bool:
        """ Tries to login into dragex.
            Returns true, if login successful and false otherwise.
        """
        pass

    def logout(self) -> bool:
        """ Tries to logout into dragex.
            Returns true, if login successful and false otherwise.
        """
        pass

    def start(self) -> None:
        """ Starts constant communication with server. """
        pass
