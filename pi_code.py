from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
motor = 0



def rotate_clockwise():
    kit.servo[motor].angle = 10
    time.sleep(10)
    kit.servo[motor].angle = 20
    time.sleep(10)
    kit.servo[motor].angle = 30
    time.sleep(10)
    kit.servo[motor].angle = 40
    time.sleep(10)
    kit.servo[motor].angle = 50
    time.sleep(10)

rotate_clockwise()
