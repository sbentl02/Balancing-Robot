from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

for i in range(10):
    kit.servo[0].angle = i * 10

