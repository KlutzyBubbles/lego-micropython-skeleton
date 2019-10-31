from pybricks.parameters import Stop

class DriveBase():
    """Class representing a robotic vehicle with two powered wheels and optional wheel caster(s).

    :param left_motor: The motor that drives the left wheel.
    :type left_motor: :class:`~ev3devices.Motor`
    :param right_motor: The motor that drives the right wheel.
    :type right_motor: :class:`~ev3devices.Motor`
    :param wheel_diameter: Diameter of the wheels.
    :type wheel_diameter: :ref:`dimension`
    :param axle_track: Distance between the midpoints of the two wheels.
    :type axle_track: :ref:`dimension`

    Example:

    .. code-block:: python

        # Initialize two motors and a drive base
        left = Motor(Port.B)
        right = Motor(Port.C)
        robot = DriveBase(left, right, 56, 114)
    """

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

    def drive(self, speed, steering):
        """Start driving at the specified speed and turnrate, both measured at the center point between the wheels of the robot.

        :param speed: Forward speed of the robot.
        :type speed: :ref:`travelspeed`
        :param steering: Turn rate of the robot.
        :type steering: :ref:`speed`

        Example:

        .. code-block:: python

            # Initialize two motors and a drive base
            left = Motor(Port.B)
            right = Motor(Port.C)
            robot = DriveBase(left, right, 56, 114)

            # Initialize a sensor
            sensor = UltrasonicSensor(Port.S4)

            # Drive forward until an object is detected
            robot.drive(100, 0)
            while sensor.distance() > 500:
                wait(10)
            robot.stop()
        """
        return

    def drive_time(self, speed, steering, time):
        """Drive at the specified speed and turnrate for a given amount of time, and then stop.

        :param speed: Forward speed of the robot.
        :type speed: :ref:`travelspeed`
        :param steering: Turn rate of the robot.
        :type steering: :ref:`speed`
        :param time: Duration of the maneuver.
        :type time: :ref:`time`

        Example:

        .. code-block:: python

            # Drive forward at 100 mm/s for two seconds
            robot.drive(100, 0, 2000)

            # Turn at 45 deg/s for three seconds
            robot.drive(0, 45, 3000)
        """
        return

    def stop(self, stop_type=Stop.COAST):
        """Stop the robot.

        :param stop_type: Whether to coast, brake, or hold (Default: :data:`~parameters.Stop.COAST`).
        :type stop_type: :class:`~parameters.Stop`
        """
        return
