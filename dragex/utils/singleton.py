class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init()

        return cls._instance

    def init(self):
        """ Performs initialization for the Singleton. """
        pass
