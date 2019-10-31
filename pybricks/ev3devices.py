from pybricks.parameters import Stop, Direction

class Motor():
    """LEGO® MINDSTORMS® EV3 Medium or Large Motor.

    Element 99455/6148292 or 95658/6148278, contained in:

    * 31313: LEGO® MINDSTORMS® EV3 (2013)
    * 45544: LEGO® MINDSTORMS® Education EV3 Core Set (2013)
    * 45503 or 45502: Separate part (2013)

    :param port: Port to which the motor is connected.
    :type port: :class:`~parameters.Port`
    :param direction: Positive speed direction (Default: :attr:`~parameters.Direction.CLOCKWISE`).
    :type direction: :class:`~parameters.Direction`
    :param gears: List of gears linked to the motor (Default: ``None``).

    For example: ``[12, 36]`` represents a gear train with a 12-tooth and a 36-tooth gear. See ratio for illustrated examples.

    Use a list of lists for multiple gear trains, such as ``[[12, 36], [20, 16, 40]]``.

    When you specify a gear train, all motor commands and settings are automatically adjusted to account for the resulting gear ratio. The motor direction remains unchanged, no matter how many gears you choose.

    For example, with ``gears=[12, 36]``, the gear ratio is 3, which means that the output is mechanically slowed down by a factor of 3. To compensate, the motor will automatically turn 3 times as fast and 3 times as far when you give a motor command. So when you choose ``run_angle(200, 90)``, your mechanism output simply turns at 200 deg/s for 90 degrees.

    The same holds for the documentation below: When it states “motor angle” or “motor speed”, you can read this as “mechanism output angle” and “mechanism output speed”, and so on, as the gear ratio is automatically accounted for.

    The ``gears`` setting is only available for motors with rotation sensors.
    :type gears: list
    """

    def __init__(self, port, direction=Direction.CLOCKWISE, gears=None):
        self.port = port
        self.direction = direction
        self.gears = gears

    def dc(self, duty):
        """Set the duty cycle of the motor.

        :param duty: The duty cycle (-100.0 to 100.0).
        :type duty: :ref:`percentage`

        Examples:

        .. code-block:: python

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)
        """
        return

    def angle(self):
        """Get the rotation angle of the motor.

        :return: Motor angle.
        :rtype: :ref:`angle`
        """
        return

    def reset_angle(self, angle):
        """Reset the accumulated rotation angle of the motor.

        :param angle: Value to which the angle should be reset.
        :type angle: :ref:`angle`
        """
        return

    def speed(self):
        """Get the speed (angular velocity) of the motor.

        :return: Motor speed.
        :rtype: :ref:`speed`
        """
        return

    def stop(self, stop_type=Stop.COAST):
        """Stop the motor.

        :param stop_type: Whether to coast, brake, or hold (Default: :data:`~parameters.Stop.COAST`).
        :type stop_type: :class:`~parameters.Stop`
        """
        return

    def run(self, speed):
        """Keep the motor running at a constant speed (angular velocity).

        The motor will accelerate towards the requested speed and the duty cycle is automatically adjusted to keep the speed constant, even under some load. This continues in the background until you give the motor a new command or the program stops.

        :param speed: Speed of the motor.
        :type speed: :ref:`speed`
        """
        return

    def run_time(self, speed, time, stop_type=Stop.COAST, wait=True):
        """Run the motor at a constant speed (angular velocity) for a given amount of time.

        The motor will accelerate towards the requested speed and the duty cycle is automatically adjusted to keep the speed constant, even under some load. It begins to decelerate just in time to reach standstill after the specified duration.

        :param speed: Speed of the motor.
        :type speed: :ref:`speed`
        :param time: Duration of the maneuver.
        :type time: :ref:`time`
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill (Default: :attr:`~parameters.Stop.COAST`).
        :type stop_type: :class:`~parameters.Stop`
        :param wait: Wait for the maneuver to complete before continuing with the rest of the program (Default: ``True``). This means that your program waits for the specified ``time``.
        :type wait: bool
        """
        return

    def run_angle(self, speed, rotation_angle, stop_type=Stop.COAST, wait=True):
        """Run the motor at a constant speed (angular velocity) by a given angle.

        The motor will accelerate towards the requested speed and the duty cycle is automatically adjusted to keep the speed constant, even under some load. It begins to decelerate just in time so that it comes to a standstill after traversing the given angle.

        :param speed: Speed of the motor.
        :type speed: :ref:`speed`
        :param rotation_angle: Angle by which the motor should rotate.
        :type rotation_angle: :ref:`angle`
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill (Default: :const:`~parameters.Stop.COAST`).
        :type stop_type: :class:`~parameters.Stop`
        :param wait: Wait for the maneuver to complete before continuing with the rest of the program (Default: ``True``). This means that your program waits for the specified ``time``.
        :type wait: bool
        """
        return

    def run_target(self, speed, target_angle, stop_type=Stop.COAST, wait=True):
        """Run the motor at a constant speed (angular velocity) towards a given target angle.

        The motor will accelerate towards the requested speed and the duty cycle is automatically adjusted to keep the speed constant, even under some load. It begins to decelerate just in time so that it comes to a standstill at the given target angle.

        The direction of rotation is automatically selected based on the target angle.

        :param speed: Absolute speed of the motor. The direction will be automatically selected based on the target angle: it makes no difference if you specify a positive or negative speed.
        :type speed: :ref:`speed`
        :param target_angle: Target angle that the motor should rotate to, regardless of its current angle.
        :type target_angle: :ref:`angle`
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill (Default: :const:`~parameters.Stop.COAST`).
        :type stop_type: :class:~parameters.Stop`
        :param wait: Wait for the maneuver to complete before continuing with the rest of the program (Default: ``True``). This means that your program waits for the specified ``time``.
        :type wait: bool
        """
        return

    def track_target(self, target_angle):
        """Track a target angle that varies in time.

        This function is quite similar to :meth:`~ev3devices.Motor.run_target()`, but speed and acceleration settings are ignored: it will move to the target angle as fast as possible. Instead, you adjust speed and acceleration by choosing how fast or slow you vary the ``target_angle``.

        This method is useful in fast loops where the motor target changes continuously.

        :param target_angle: Target angle that the motor should rotate to.
        :type target_angle: :ref:`angle`

        Example:

        .. code-block:: python

            # Initialize motor and timer
            from math import sin
            motor = Motor(Port.A)
            watch = StopWatch()
            amplitude = 90

            # In a fast loop, compute a reference angle
            # and make the motor track it.
            while True:
                # Get the time in seconds
                seconds = watch.time()/1000
                # Compute a reference angle. This produces
                # a sine wave that makes the motor move
                # smoothly between -90 and +90 degrees.
                angle_now = sin(seconds)*amplitude
                # Make the motor track the given angle
                motor.track_target(angle_now)
        """
        return

    def stalled(self):
        """Check whether the motor is currently stalled.

        A motor is stalled when it cannot move even with the maximum torque. For example, when something is blocking the motor or your mechanism simply cannot turn any further.

        Specifically, the motor is stalled when the duty cycle computed by the PID controllers has reached the maximum (so ``duty`` = ``duty_limit``) and still the motor cannot reach a minimal speed (so ``speed`` < ``stall_speed``) for a period of at least ``stall_time``.

        You can change the ``duty_limit``, ``stall_speed``, and ``stall_time`` settings using :meth:`~ev3devices.Motor.set_dc_settings()` and :meth:`~ev3devices.Motor.set_pid_settings()` in order to change the sensitivity to being stalled.

        :return: ``True`` if the motor is stalled, ``False`` if it is not.
        :rtype: bool
        """
        return

    def run_until_stalled(self, speed, stop_type=Stop.COAST, duty_limit=100):
        """Run the motor at a constant speed (angular velocity) until it stalls. The motor is considered stalled when it cannot move even with the maximum torque. See stalled() for a more precise definition.

        The ``duty_limit`` argument lets you temporarily limit the motor torque during this maneuver. This is useful to avoid applying the full motor torque to a geared or lever mechanism.

        :param speed: Speed of the motor.
        :type speed: :ref:`speed`
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill (Default: :const:`~parameters.Stop.COAST`).
        :type stop_type: :class:`~parameters.Stop`
        :param duty_limit: Relative torque limit. This limit works just like :meth:`~ev3devices.Motor.set_dc_settings()`, but in this case the limit is temporary: it returns to its previous value after completing this command.
        :type duty_limit: :ref:`percentage`
        """
        return

    def set_dc_settings(self, duty_limit, duty_offset):
        """Configure the settings to adjust the behavior of the :meth:`~ev3devices.Motor.dc()` command. This also affects all of the ``run`` commands, which use the :meth:`~ev3devices.Motor.dc()` method in the background.

        :param duty_limit: Relative torque limit during subsequent motor commands. This sets the maximum duty cycle that is applied during any subsequent motor command. This reduces the maximum torque output to a percentage of the absolute maximum stall torque. This is useful to avoid applying the full motor torque to a geared or lever mechanism, or to prevent your LEGO® train from unintentionally going at full speed. (Default: 100).
        :type duty_limit: :ref:`percentage`
        :param duty_offset: Minimum duty cycle given when you use :meth:`~ev3devices.Motor.dc()`. This adds a small feed forward torque so that your motor will move even for very low duty cycle values, which can be useful when you create your own feedback controllers (Default: 0).
        :type duty_offset: :ref:`percentage`
        """
        return

    def set_run_settings(self, max_speed, acceleration):
        """Configure the maximum speed and acceleration/deceleration of the motor for all run commands.

        This applies to the ``run``, ``run_time``, ``run_angle``, ``run_target``, or ``run_until_stalled`` commands you give the motor. See also the default parameters for each motor.

        :param max_speed: Maximum speed of the motor during a motor command.
        :type max_speed: :ref:`speed`
        :param acceleration: Acceleration towards the target speed and deceleration towards standstill. This should be a positive value. The motor will automatically change the sign to decelerate as needed.
        :type acceleration: :ref:`acceleration`

        Example:

        .. code-block:: python

            # Set the maximum speed to 200 deg/s and acceleration to 400 deg/s/s.
            example_motor.set_run_settings(200, 400)

            # Make the motor run for 5 seconds. Even though the speed argument is 300
            # deg/s in this example, the motor will move at only 200 deg/s because of
            # the settings above.
            example_motor.run_time(300, 5000)
        """
        return

    def set_pid_settings(self, kp, ki, kd, tight_loop_limit, angle_tolerance, speed_tolerance, stall_speed, stall_time):
        """Configure the settings of the position and speed controllers. See also pid and the default parameters for each motor.

        :param kp: Proportional position (and integral speed) control constant.
        :type kp: int
        :param ki: Integral position control constant.
        :type ki: int
        :param kd: Derivative position (and proportional speed) control constant.
        :type kd: int
        :param tight_loop_limit: If you execute any of the ``run`` commands within this interval after starting the previous command, the controllers assume that you want to control the speed directly. This means that it will ignore the acceleration setting and immediately begin tracking the speed you give in the ``run`` command. This is useful in a fast loop, where you usually want the motors to respond quickly rather than accelerate smoothly, for example with a line-following robot.
        :type tight_loop_limit: :ref:`time`
        :param angle_tolerance: Allowed deviation from the target angle before motion is considered complete.
        :type angle_tolerance: :ref:`angle`
        :param speed_tolerance: Allowed deviation from zero speed before motion is considered complete.
        :type speed_tolerance: :ref:`speed`
        :param stall_speed: See :meth:`~ev3devices.Motor.stalled()`
        :type stall_speed: :ref:`speed`
        :param stall_time: See :meth:`~ev3devices.Motor.stalled()`
        :type stall_time: :ref:`time`
        """
        return

class TouchSensor():
    """LEGO® MINDSTORMS® EV3 Touch Sensor.

    Element 95648/6138404, contained in:

    * 31313: LEGO® MINDSTORMS® EV3 (2013)
    * 45544: LEGO® MINDSTORMS® Education EV3 Core Set (2013)
    * 45507: Separate part (2013)

    :param port: Port to which the sensor is connected.
    :type port: :class:`~parameters.Port`
    """
    def __init__(self, port):
        self.port = port

    def pressed(self):
        """Check if the sensor is pressed.

        :return: ``True`` if the sensor is pressed, ``False`` if it is not pressed.
        :rtype: bool
        """
        return

class ColorSensor():
    """LEGO® MINDSTORMS® EV3 Color Sensor.

    Element 95650/6128869, contained in:

    * 31313: LEGO® MINDSTORMS® EV3 (2013)
    * 45544: LEGO® MINDSTORMS® Education EV3 Core Set (2013)
    * 45506: Separate part (2013)

    :param port: Port to which the sensor is connected.
    :type port: :class:`~parameters.Port`
    """

    def __init__(self, port):
        self.port = port

    def color(self):
        """Measure the color of a surface.

        :return: ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``, ``Color.YELLOW``, ``Color.RED``, ``Color.WHITE``, ``Color.BROWN`` or ``None``.
        :rtype: :class:`~parameters.Color`, or ``None`` is no color is detected.
        """
        return

    def ambient(self):
        """Measure the ambient light intensity.

        :return: Ambient light intensity, ranging from 0 (dark) to 100 (bright).
        :rtype: :ref:`percentage`
        """
        return

    def reflection(self):
        """Measure the reflection of a surface using a red light.

        :return: Reflection, ranging from 0 (no reflection) to 100 (high reflection).
        :rtype: :ref:`percentage`
        """
        return

    def rgb(self):
        """Measure the reflection of a surface using a red, green, and then a blue light.

        :return: Reflection for red, green, and blue light, each ranging from 0.0 (no reflection) to 100.0 (high reflection).
        :rtype: tuple of three :ref:`percentage`
        """
        return

class InfraredSensor():
    """LEGO® MINDSTORMS® EV3 Infrared Sensor and Beacon.

    Element 95654/6132629 and 72156/6127283, contained in:

    * 31313: LEGO® MINDSTORMS® EV3 (2013)
    * 45509 and 45508: Separate parts (2013)

    :param port: Port to which the sensor is connected.
    :type port: :class:`~parameters.Port`
    """

    def __init__(self, port):
        self.port = port

    def distance(self):
        """Measure the relative distance between the sensor and an object using infrared light.

        :return: Relative distance ranging from 0 (closest) to 100 (farthest).
        :rtype: :ref:`relativedistance`
        """
        return

    def beacon(self, channel):
        """Measure the relative distance and angle between the remote and the infrared sensor.

        :param channel:  Channel number of the remote.
        :type channel: int

        :return: Tuple of relative distance (0 to 100) and approximate angle (-75 to 75 degrees) between remote and infrared sensor.
        :rtype: (:ref:`relativedistance`, :ref:`angle`) or (``None``, ``None``) if no remote is detected.
        """
        return

    def buttons(self, channel):
        """Check which buttons on the infrared remote are pressed.

        :param channel:  Channel number of the remote.
        :type channel: int

        :return: List of pressed buttons on the remote on the specified channel.
        :rtype: List of :class:`~parameters.Button`
        """
        return

class UltrasonicSensor():
    """LEGO® MINDSTORMS® EV3 Ultrasonic Sensor.

    Element 95652/6138403, contained in:

    * 45544: LEGO® MINDSTORMS® Education EV3 Core Set (2013)
    * 45504: Separate part (2013)

    :param port: Port to which the sensor is connected.
    :type port: :class:`~parameters.Port`
    """

    def __init__(self, port):
        self.port = port

    def distance(self, silent=False):
        """Measure the distance between the sensor and an object using ultrasonic sound waves.

        :param silent: Choose ``True`` to turn the sensor off after measuring the distance.

        Choose ``False`` to leave the sensor on (Default).

        When you choose ``silent=True``, the sensor does not emit sounds waves except when taking the measurement. This reduces interference with other ultrasonic sensors, but turning the sensor off takes approximately 300 ms each time.
        :type silent: bool

        :return: Distance (millimeters).
        :rtype: :ref:`distance`
        """
        return

    def presence(self):
        """Check for the presence of other ultrasonic sensors by detecting ultrasonic sounds.

        If the other ultrasonic sensor is operating in silent mode, you can only detect the presence of that sensor while it is taking a measurement.

        :return: ``True`` if ultrasonic sounds are detected, ``False`` if not.
        :rtype: bool
        """
        return

class GyroSensor():
    """LEGO® MINDSTORMS® EV3 Gyro Sensor.

    Element 99380/6138411, contained in:

    * 45544: LEGO® MINDSTORMS® Education EV3 Core Set (2013)
    * 45505: Separate part (2013)

    :param port: Port to which the sensor is connected.
    :type port: :class:`~parameters.Port`
    :param direction:  Positive rotation direction when looking at the red dot on top of the sensor (Default: :attr:`~parameters.Direction.CLOCKWISE`).
    :type direction: :class:`~parameters.Direction`
    """

    def __init__(self, port, direction=Direction.CLOCKWISE):
        self.port = port
        self.direction = direction

    def speed(self):
        """Get the speed (angular velocity) of the sensor.

        :return: Sensor angular velocity.
        :rtype: :ref:`speed`
        """
        return

    def angle(self):
        """Get the accumulated angle of the sensor.

        :return: Rotation angle.
        :rtype: :ref:`angle`
        """
        return

    def reset_angle(self, angle):
        """Set the rotation angle of the sensor to a desired value.

        :param angle: Value to which the angle should be reset.
        :type angle: :ref:`angle`
        """
        return
