from sn3218 import sn3218

class PiGlow(sn3218):

        legs = [
                [ 6, 7, 8, 5, 4, 9 ],
                [ 17, 16, 15, 13, 11, 10 ],
                [ 0, 1, 2, 3, 14, 12 ]
        ]

        def __init__(self, i2c_bus=1):
                sn3218.__init__(self, i2c_bus)

        def ring(self, ring, intensity):
                self.set([self.legs[0][ring], self.legs[1][ring], self.legs[2][ring]], intensity)
                self.update()

        def leg(self, leg, intensity):
                self.set(self.legs[leg], intensity)
                self.update()

        def led(self, leg, ring, intensity):
                self.set(self.legs[leg][ring], intensity)
                self.update()

        def clear(self):
                self.set(0, [0]*18)
                self.update()
