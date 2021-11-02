from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
motor = 0



def rotate_clockwise():
    kit.servo[motor].angle = 10
    time.sleep(0.01)
    kit.servo[motor].angle = 20
    time.sleep(0.01)    
    kit.servo[motor].angle = 30
    time.sleep(0.01)
    kit.servo[motor].angle = 40
    time.sleep(0.01)
    kit.servo[motor].angle = 50

rotate_clockwise()

time.sleep(10)
kit.servo[motor].angle = 0
