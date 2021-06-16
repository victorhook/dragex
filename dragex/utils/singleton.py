class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        return cls.instance(*args, **kwargs)

    def init(self, *args, **kwargs):
        """ Performs initialization for the Singleton. """
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init(*args, **kwargs)

        return cls._instance
