from __future__ import print_function
from sys import stdout
import builtins

def print(*value, sep=' ', end='\n', file=stdout, flush=False):
    # pylint: disable=redefined-builtin
    """Print values on the terminal or a stream.

    Example:

    .. code-block:: python

        # Print some text
        print("Hello, world")

        # Print some text and a number
        print("Value:", 5)
    """
    return builtins.print(value, sep=sep, end=end, file=file, flush=flush)

def wait(time):
    """Pause the user program for a specified amount of time.

    :param time: How long to wait.
    :type time: :ref:`time`
    """
    return

class StopWatch():
    """
    A stopwatch to measure time intervals. Similar to the stopwatch feature on your phone.
    """

    def time(self):
        """Get the current time of the stopwatch.

        :return: Elapsed time.
        :rtype: :ref:`time`
        """
        return

    def pause(self):
        """
        Pause the stopwatch.
        """
        return

    def resume(self):
        """
        Resume the stopwatch.
        """
        return

    def reset(self):
        """
        Reset the stopwatch time to 0.

        The run state is unaffected:

        * If it was paused, it stays paused (but now at 0).
        * If it was running, it stays running (but starting again from 0).
        """
        return
