import os
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

class Motor():
    def __init__(self):
        #define GPIO pins
        self.GPIO_pins = (26, 5, 6) # Microstep Resolution MS1-MS3 -> GPIO Pin
        self.direction= 16          # Direction -> GPIO Pin
        self.step = 13              # Step -> GPIO Pin

        # Declare an named instance of class pass GPIO pins numbers
        self.mymotor = RpiMotorLib.A4988Nema(self.direction, self.step, self.GPIO_pins, "A4988")

    def change_motor_position(self, direction):
        # lines = []

        # with open("/etc/profile", 'r') as profile:
        #     lines = profile.readlines()
        #     new_pos = str(int(os.environ["CURRENT_POS"]) + direction)
        #     new_last_line = "export CURRENT_POS=" + new_pos
        #     lines[-1] = new_last_line

        # with open("/etc/profile", 'w') as profile:
        #     profile.writelines(lines)
        os.environ["CURRENT_POS"] = str(int(os.environ["CURRENT_POS"]) + direction)

    def open_clock(self):
        if int(os.environ["CURRENT_POS"]) + 1 < int(os.environ["MAX_CLOSED"]):
            self.mymotor.motor_go(True, "Full", 1, .00000000000001, False, .05)
            self.change_motor_position(1)

    def open_anticlock(self):
        if int(os.environ["CURRENT_POS"]) - 1 >= int(os.environ["MAX_OPEN"]):
            self.mymotor.motor_go(False, "Full", 1, .00000000000001, False, .05)
            self.change_motor_position(-1)

