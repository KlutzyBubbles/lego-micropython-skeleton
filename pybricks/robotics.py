from pybricks.parameters import Stop

class DriveBase():

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

    def drive(self, speed, steering):
        return

    def drive_time(self, speed, steering, time):
        return

    def stop(self, stop_type=Stop.COAST):
        return