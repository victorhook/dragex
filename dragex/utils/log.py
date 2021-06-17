import logging

global LOGGER
LOGGER = None

logging.basicConfig(level=logging.DEBUG)


_SILENCE_LOGS = [
    'PIL'
]


def get_logger() -> logging.Logger:
    global LOGGER
    if LOGGER is None:
        LOGGER = logging.getLogger()
        for log in _SILENCE_LOGS:
            logging.getLogger(log).setLevel(logging.WARNING)

    return LOGGER
