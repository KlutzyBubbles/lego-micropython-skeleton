from pybricks.parameters import Align

def buttons():
    """Check which buttons on the EV3 Brick are currently pressed.

    :return: List of pressed buttons.
    :rtype: List of ``Button``

    Examples:

    .. code-block:: python

        # Do something if the left button is pressed
        if Button.LEFT in brick.buttons():
            print("The left button is pressed.")

    .. code-block:: python

        # Wait until any of the buttons are pressed
        while not any(brick.buttons()):
            wait(10)

        # Wait until all buttons are released
        while any(brick.buttons()):
            wait(10)
    """
    return

def light(color):
    """Play a beep/tone

    :param color: Color of the light. Choose ``Color.BLACK`` or ``None`` to turn the light off.
    :type color: :class:`~parameters.Color`

    Example:

    .. code-block:: python

        # Make the light red
        brick.light(Color.RED)

        # Turn the light off
        brick.light(None)
    """
    return

class sound():

    @staticmethod
    def beep(frequency=500, duration=100, volume=30):
        """Play a beep/tone

        :param frequency: Frequency of the beep (Default: 500).
        :type frequency: :ref:`frequency`
        :param duration: Duration of the beep (Default: 100).
        :type duration: :ref:`time`
        :param volume: Volume of the beep (Default: 30).
        :type volume: :ref:`percentage`

        Example:

        .. code-block:: python

            # A simple beep
            brick.sound.beep()

            # A high pitch (1500 Hz) for one second (1000 ms) at 50% volume
            brick.sound.beep(1500, 1000, 50)
        """
        return

    @staticmethod
    def beeps(number):
        """Play a number of default beeps with a brief pause in between.

        :param number: Number of beeps.
        :type number: int

        Example:

        .. code-block:: python

            # Make 5 simple beeps
            brick.sound.beeps(5)
        """
        return

    @staticmethod
    def file(file_name, volume=100):
        """Play a sound file.

        :param file_name: Path to the sound file, including extension.
        :type file_name: str
        :param volume: Volume of the sound (Default: 100).
        :type volume: :ref:`percentage`

        Example:

        .. code-block:: python

            # Play one of the built-in sounds
            brick.sound.file(SoundFile.HELLO)

            # Play a sound file from your project folder
            brick.sound.file('mysound.wav')
        """
        return

class display():

    @staticmethod
    def clear():
        """
        Clear everything on the display.
        """
        return

    @staticmethod
    def text(text, coordinate=None):
        """Play a sound file.

        :param text: The text to display.
        :type text: str
        :param coordinate: ``(x, y)`` coordinate tuple. It is the top-left corner of the first character. If no coordinate is specified, it is printed on the next line.
        :type coordinate: tuple

        Example:

        .. code-block:: python

            # Clear the display
            brick.display.clear()

            # Print ``Hello`` near the middle of the screen
            brick.display.text("Hello", (60, 50))

            # Print ``World`` directly underneath it
            brick.display.text("World")
        """
        return

    @staticmethod
    def image(file_name, alignment=Align.CENTER, coordinate=None, clear=True):
        """Show an image file.

        You can specify its placement either using ``alignment`` or by specifying a ``coordinate``, but not both.

        :param file_name: Path to the image file. Paths may be absolute or relative from the project folder.
        :type file_name: str
        :param alignment: Where to place the image (Default: Align.CENTER).
        :type alignment: :class:`~parameters.Align`
        :param coordinate: ``(x, y)`` coordinate tuple. It is the top-left corner of the image (Default: None).
        :type coordinate: tuple
        :param clear: Whether to clear the screen before showing the image (Default: ``True``).
        :type clear: bool

        Example:

        .. code-block:: python

            # Show a built-in image of two eyes looking upward
            brick.display.image(ImageFile.UP)

            # Display a custom image from your project folder
            brick.display.image('pybricks.png')

            # Display a custom image at the top right of the screen, without clearing
            # the screen first
            brick.display.image('arrow.png', Align.TOP_RIGHT, clear=False)
        """
        return

class battery():

    @staticmethod
    def voltage():
        """Get the voltage of the battery.

        :return: Battery voltage.
        :rtype: :ref:`voltage`

        Example:

        .. code-block:: python

            # Play a warning sound when the battery voltage
            # is below 7 Volt (7000 mV = 7V)
            if brick.battery.voltage() < 7000:
                brick.sound.beep()
        """
        return

    @staticmethod
    def current():
        """Get the current supplied by the battery.

        :return: Battery current.
        :rtype: :ref:`current`
        """
        return
