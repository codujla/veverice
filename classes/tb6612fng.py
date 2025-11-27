#motor driver

from machine import Pin, PWM

class Motor:
    def __init__(self, in1, in2, pwm_pin, freq=20000):
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)

        self.pwm = PWM(Pin(pwm_pin))
        self.pwm.freq(freq)  #pwm frekvencija
        self.stop()

    def _set_direction(self, forward):
        if forward:
            self.in1.value(1)
            self.in2.value(0)
        else:
            self.in1.value(0)
            self.in2.value(1)

    def _set_speed(self, speed_percent):
        speed_percent = max(0, min(100, speed_percent))
        duty = int(speed_percent * 655)   # 100% -> 65535/100 -> 655 per percent
        self.pwm.duty_u16(duty)

    def forward(self, speed):
        self._set_direction(True)
        self._set_speed(speed)

    def backward(self, speed):
        self._set_direction(False)
        self._set_speed(speed)

    def stop(self):
        self.in1.value(0)
        self.in2.value(0)
        self.pwm.duty_u16(0)

    def drive(self, speed):
        if speed > 0:
            self.forward(speed)
        elif speed < 0:
            self.backward(abs(speed))
        else:
            self.stop()
