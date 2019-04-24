from pybricks.parameters import Stop, Direction

class Motor():

    def __init__(self, port, direction=Direction.CLOCKWISE, gears=None):
        self.port = port
        self.direction = direction
        self.gears = gears

    def dc(self, duty):
        return

    def angle(self):
        return

    def reset_angle(self, angle):
        return

    def speed(self):
        return

    def stop(self, stop_type=Stop.COAST):
        return

    def run(self, speed):
        return

    def run_time(self, speed, time, stop_type=Stop.COAST, wait=True):
        return

    def run_angle(self, speed, rotation_angle, stop_type=Stop.COAST, wait=True):
        return

    def run_target(self, speed, target_angle, stop_type=Stop.COAST, wait=True):
        return

    def track_target(self, target_angle):
        return

    def stalled(self):
        return

    def run_until_stalled(self, speed, stop_type=Stop.COAST, duty_limit=100):
        return

    def set_dc_settings(self, duty_limit, duty_offset):
        return

    def set_run_settings(self, max_speed, acceleration):
        return

    def set_pid_settings(self, kp, ki, kd, tight_loop_limit, angle_tolerance, speed_tolerance, stall_speed, stall_time):
        return

class TouchSensor():

    def __init__(self, port):
        self.port = port

    def pressed(self):
        return

class ColorSensor():

    def __init__(self, port):
        self.port = port

    def color(self):
        return

    def ambient(self):
        return

    def reflection(self):
        return

    def rgb(self):
        return

class InfraredSensor():

    def __init__(self, port):
        self.port = port

    def distance(self):
        return

    def beacon(self, channel):
        return

    def buttons(self, channel):
        return

class UltrasonicSensor():

    def __init__(self, port):
        self.port = port

    def distance(self, silent=False):
        return

    def presence(self):
        return

class GyroSensor():

    def __init__(self, port, direction=Direction.CLOCKWISE):
        self.port = port
        self.direction = direction

    def speed(self):
        return

    def angle(self):
        return

    def reset_angle(self, angle):
        return
