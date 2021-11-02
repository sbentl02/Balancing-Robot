from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
motor = 0
STOP = -0.1

kit.continuous_servo[motor].throttle = STOP
time.sleep(1)

def rotate_clockwise():
    kit.continuous_servo[motor].throttle = 1
    time.sleep(0.054)
    kit.continuous_servo[motor].throttle = STOP


rotate_clockwise()

time.sleep(10)
kit.servo[motor].angle = 0
