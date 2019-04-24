from __future__ import print_function
from sys import stdout
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

def print(*value, sep=' ', end='\n', file=stdout, flush=False):
    return __builtin__.print(value, sep=sep, end=end, file=file, flush=flush)

def wait(time):
    return

class StopWatch():

    def time(self):
        return

    def pause(self):
        return

    def resume(self):
        return

    def reset(self):
        return
