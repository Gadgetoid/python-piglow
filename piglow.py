import sn3218

sn3218.enable()
sn3218.enable_leds(0b111111111111111111)

legs = [
  [ 6, 7, 8, 5, 4, 9 ],
  [ 17, 16, 15, 13, 11, 10 ],
  [ 0, 1, 2, 3, 14, 12 ]
]

values = [0] * 18

colours = {
  "red" : 0,
  "orange" : 1,
  "yellow" : 2,
  "green" : 3,
  "blue" : 4,
  "white" : 5
}

white  = lambda v: ring(5,v)
blue   = lambda v: ring(4,v)
green  = lambda v: ring(3,v)
yellow = lambda v: ring(2,v)
orange = lambda v: ring(1,v)
red    = lambda v: ring(0,v)

led1   = lambda v: set(0,v)
led2   = lambda v: set(1,v)
led3   = lambda v: set(2,v)
led4   = lambda v: set(3,v)
led5   = lambda v: set(4,v)
led6   = lambda v: set(5,v)
led7   = lambda v: set(6,v)
led8   = lambda v: set(7,v)
led9   = lambda v: set(8,v)
led10  = lambda v: set(9,v)
led11  = lambda v: set(10,v)
led12  = lambda v: set(11,v)
led13  = lambda v: set(12,v)
led14  = lambda v: set(13,v)
led15  = lambda v: set(14,v)
led16  = lambda v: set(15,v)
led17  = lambda v: set(16,v)
led18  = lambda v: set(17,v)			

def show():
  sn3218.output(values)

def set(leds, value):
  if isinstance(leds, list):
    for led in leds:
      if isinstance(value, list):
        values[leds[led]] = value[led]
      else:
        values[led] = value
  elif isinstance(leds, int):
    values[leds] = value
  else:
    raise ValueError("Invalid LED/LEDs")

def ring(ring, intensity):
  set([legs[0][ring], legs[1][ring], legs[2][ring]], intensity)


def leg_bar(leg, percentage):
  # 1530 = 6 * 255
  amount = int(1530.0 * percentage)
  for led in reversed(legs[leg]):
    if amount >= 255:
      set(led, 255)
    elif amount > 0:
      set(led,amount)
    else:
      set(led,0)
    amount = amount - 255

def leg(leg, intensity):
  set(legs[leg], intensity)
	
def arm(arm, intensity):
  set(legs[arm-1], intensity)

def arm1(intensity):
  arm(1, intensity)

def arm2(intensity):
  arm(2, intensity)

def arm3(intensity):
  arm(3, intensity)

def led(led, intensity):
  set(led-1, intensity)

def single(leg, ring, intensity):
  set(legs[leg][ring], intensity)

def colour(colour, intensity):
  if not isinstance(colour, int):
    if colour in colours:
      colour = colours[colour]
      ring(colour, intensity)
      return True
    else:
      raise ValueError("Invalid Colour")
      return False
  ring(colour-1, intensity)
  return True
	
def all(value):
  set(0, [value]*18)

def clear():
  set(0, [0]*18)