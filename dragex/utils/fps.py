import time


class Fps:

    def __init__(self):
        self.count = 0
        self._last_fps = 0
        self.t0 = time.time()

    def inc(self):
        self.count += 1

        t1 = time.time()
        if t1 - self.t0 > 1:
            self.t0 = t1
            self._last_fps = self.count
            self.count = 0

    def read(self):
        return self._last_fps
