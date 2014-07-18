from sn3218 import sn3218

class PiGlow(sn3218):

        legs = [
                [ 6, 7, 8, 5, 4, 9 ],
                [ 17, 16, 15, 13, 11, 10 ],
                [ 0, 1, 2, 3, 14, 12 ]
        ]

	colours = {
		"red" : 0,
		"orange" : 1,
		"yellow" : 2,
		"green" : 3,
		"blue" : 4,
		"white" : 5
	}

        def __init__(self, i2c_bus=1):
                sn3218.__init__(self, i2c_bus)
		setattr(self, 'white',  lambda v: self.ring(5,v))
		setattr(self, 'blue',   lambda v: self.ring(4,v))
                setattr(self, 'green',  lambda v: self.ring(3,v))
                setattr(self, 'yellow', lambda v: self.ring(2,v))
                setattr(self, 'orange', lambda v: self.ring(1,v))
                setattr(self, 'red',    lambda v: self.ring(0,v))

		setattr(self, 'led1', lambda v: self.set(0,v))
                setattr(self, 'led2', lambda v: self.set(1,v))
                setattr(self, 'led3', lambda v: self.set(2,v))
                setattr(self, 'led4', lambda v: self.set(3,v))
                setattr(self, 'led5', lambda v: self.set(4,v))
                setattr(self, 'led6', lambda v: self.set(5,v))
                setattr(self, 'led7', lambda v: self.set(6,v))
                setattr(self, 'led8', lambda v: self.set(7,v))
                setattr(self, 'led9', lambda v: self.set(8,v))
                setattr(self, 'led10', lambda v: self.set(9,v))
                setattr(self, 'led11', lambda v: self.set(10,v))
                setattr(self, 'led12', lambda v: self.set(11,v))
                setattr(self, 'led13', lambda v: self.set(12,v))
                setattr(self, 'led14', lambda v: self.set(13,v))
                setattr(self, 'led15', lambda v: self.set(14,v))
                setattr(self, 'led16', lambda v: self.set(15,v))
                setattr(self, 'led17', lambda v: self.set(16,v))
                setattr(self, 'led18', lambda v: self.set(17,v))			

	def set(self, led, value):
		sn3218.set(self, led, value)
		self.update()

        def ring(self, ring, intensity):
                self.set([self.legs[0][ring], self.legs[1][ring], self.legs[2][ring]], intensity)

        def leg(self, leg, intensity):
                self.set(self.legs[leg], intensity)
	
	def arm(self, arm, intensity):
		self.set(self.legs[arm-1], intensity)

	def arm1(self, intensity):
		self.arm(1, intensity)

	def arm2(self, intensity):
		self.arm(2, intensity)

	def arm3(self, intensity):
		self.arm(3, intensity)

	def led(self, led, intensity):
		self.set(led-1, intensity)

        def single(self, leg, ring, intensity):
                self.set(self.legs[leg][ring], intensity)

	def colour(self, colour, intensity):
		if not isinstance(colour, int):
			if colour in self.colours:
				colour = self.colours[colour]
				self.ring(colour, intensity)
				return True
			else:
				raise ValueError("Invalid Colour")
				return False
		self.ring(colour-1, intensity)
		return True
	
	def all(self, value):
		self.set(0, [value]*18)

        def clear(self):
                self.set(0, [0]*18)
