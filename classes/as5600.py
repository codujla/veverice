#encoder AS5600

class AS5600:
    def __init__(self, i2c):
        self.i2c = i2c
        self.addr = 0x36

    def angle(self):
        data = self.i2c.readfrom_mem(self.addr, 0x0C, 2)
        raw = (data[0] << 8) | data[1]
        return raw * 360 / 4096
