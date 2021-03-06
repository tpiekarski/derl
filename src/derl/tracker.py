#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from time import perf_counter

from derl.model.stats import Stats


class Singleton(type):
    _instances = {}

    def __call__(cls: "Singleton", *args: tuple, **kwargs: dict) -> "Tracker":
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Tracker(metaclass=Singleton):
    start_time = None
    stop_time = None
    stats = Stats()
    test = False

    def start(self: "Tracker"):
        if self.start_time is None:
            self.start_time = perf_counter()

    def stop(self: "Tracker"):
        if self.stop_time is None:
            self.stop_time = perf_counter()

    def calc_time(self: "Tracker") -> float:
        if self.test:
            return -1

        return round(self.stop_time - self.start_time)

    def reset(self: "Tracker"):
        self.start_time = 0
        self.stop_time = 0
        self.stats = Stats()

    def set_test(self: "Tracker"):
        self.test = True

    def __str__(self: "Tracker") -> str:
        output = ""

        if self.start_time is not None and self.stop_time is not None:
            output += "\nFinished checking URLs after {0:.2f} second(s).\n".format(self.calc_time())

        output += self.stats.__str__()

        return output

    def __repr__(self: "Tracker") -> str:
        return self.__str__()


def get_tracker() -> "Tracker":
    return Tracker()
