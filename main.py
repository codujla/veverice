from machine import I2C, Pin
import utime
from classes.tb6612fng import Motor
from classes.tca9548 import TCA9548A
from classes.as5600 import AS5600
from classes.robot import Robot

i2c0 = I2C(0, scl=Pin(1), sda=Pin(0))
i2c1 = I2C(0, scl=Pin(3), sda=Pin(2)) 

enc0 = AS5600(i2c0)
enc1 = AS5600(i2c1)

left = Motor(in1=10, in2=11, pwm_pin=9)
right = Motor(in1=15, in2=14, pwm_pin=12)

robot = Robot(left, right)

_test = 1

def test():
    global _test
    robot.forward(60)
    utime.sleep(1)

    robot.turn_left(40)
    utime.sleep(0.7)

    robot.turn_right(80)
    utime.sleep(0.7)

    robot.turn_left(40)
    utime.sleep(0.7)

    robot.backward(30)
    utime.sleep(1)

    robot.stop()
    utime.sleep(1)

    _test = 0 

print("start")

try:
    while True:
        if _test:
            test()

        print(f"Levo: {enc0.angle():.2f}° \n")
        print(f"Desno: {enc1.angle():.2f}° \n")
        print("--------------------------------")
        utime.sleep(1)

except KeyboardInterrupt:
    robot.stop()
    print("stop")