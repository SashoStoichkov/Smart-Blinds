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

    def open_clock(self):
        self.mymotor.motor_go(True, "1/16", 1, .00000001, False, .05)

    def open_anticlock(self):
        self.mymotor.motor_go(False, "1/16", 1, .00000001, False, .05)