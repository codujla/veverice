from machine import I2C, Pin
import utime,time
from classes.tb6612fng import Motor
from classes.tca9548 import TCA9548A
from classes.as5600 import AS5600
from classes.robot import Robot

i2c = I2C(0, scl=Pin(1), sda=Pin(0))

mux = TCA9548A(i2c)
mux.select(0)

enc1 = AS5600(i2c)


left = Motor(in1=10, in2=11, pwm_pin=9)
right = Motor(in1=15, in2=14, pwm_pin=12)

robot = Robot(left, right)

_test = 1

def test():
    global _test
    robot.forward(60)
    time.sleep(1)

    robot.turn_left(40)
    time.sleep(0.7)

    robot.turn_right(80)
    time.sleep(1.5)

    robot.turn_left(40)
    time.sleep(0.7)

    robot.backward(30)
    time.sleep(1)

    robot.stop()
    time.sleep(1)

    _test = 0 

print("start")

try:
    while True:
        if _test:
            test()
        time.sleep(1)

        # mux.select(0)
        # a1 = enc1.angle()
        # print(a1)
except KeyboardInterrupt:
    print("stop")