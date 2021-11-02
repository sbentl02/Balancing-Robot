from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
motor = 0
STOP = -0.1

kit.continuous_servo[motor].throttle = STOP
time.sleep(1)

def forward_90():
    kit.continuous_servo[motor].throttle = -1
    time.sleep(10)
    kit.continuous_servo[motor].throttle = STOP

def backward_90(): 
    kit.continuous_servo[motor].throttle = 1
    time.sleep(10)
    kit.continuous_servo[motor].throttle = STOP

def rotate_clockwise():
    #Turn 90 deg
    forward_90()
    #Pause
    time.sleep(10)
    #Turn back 90 deg
    backward_90()

def rotate_counterclockwise():
    #Turn 90 deg
    backward_90()    
    #Pause
    time.sleep(10)
    #Turn back 90 deg
    forward_90()


rotate_clockwise()

time.sleep(10)
