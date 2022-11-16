
import time
from datetime import datetime


class Chronometer:

    def __init__(self) -> None:
        self.__start_d = 0
        self.__end_d = 0
        self.__start_s = 0
        self.__end_s   = 0

    @property
    def start_d(self):
        return self.__start_d

    @property
    def end_d(self):
        return self.__end_d

    @property
    def start_s(self):
        return self.__start_s

    @property
    def end_s(self):
        return self.__end_s

    def start_counting(self) -> None:
        self.__start_d = datetime.now()
        self.__start_s = time.time()

    def finish_counting(self) -> None:
        self.__end_d = datetime.now()
        self.__end_s = time.time()

    def delta_d(self):
        return self.end_d - self.start_d

    def delta_s(self):
        return self.end_s - self.start_s
