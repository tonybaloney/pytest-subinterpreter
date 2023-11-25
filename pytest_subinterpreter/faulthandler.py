import sys

class FaultHandler:
    def __init__(self):
        self._enabled = False

    def enable(self, file=sys.stderr, all_threads=True):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def is_enabled(self):
        return self._enabled

    def dump_traceback_later(self, timeout, file):
        pass

    def cancel_dump_traceback_later(self):
        pass