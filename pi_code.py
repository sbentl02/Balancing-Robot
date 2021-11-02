from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
motor = 0



def rotate_clockwise():
    kit.servo[motor].angle = 10
    kit.servo[motor].angle = 20
    kit.servo[motor].angle = 30
    kit.servo[motor].angle = 40
    kit.servo[motor].angle = 50

rotate_clockwise()

time.sleep(1)
kit.servo[motor].angle = 0
