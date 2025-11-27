class Robot:
    def __init__(self, left_motor, right_motor):
        self.left = left_motor
        self.right = right_motor

    def forward(self, speed=50):
        self.left.forward(speed)
        self.right.forward(speed)

    def backward(self, speed=50):
        self.left.backward(speed)
        self.right.backward(speed)

    def stop(self):
        self.left.stop()
        self.right.stop()

    def turn_left(self, speed=50):
        self.left.backward(speed)
        self.right.forward(speed)

    def turn_right(self, speed=50):
        self.left.forward(speed)
        self.right.backward(speed)
