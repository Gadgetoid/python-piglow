#PiGlow

This repository contains the library and examples for the PiGlow board.

## Easy Install

To install on your Raspberry Pi, make sure you're running Raspbian, open LXTerminal or make your way to the terminal and run:

```bash
curl get.pimoroni.com/piglow | bash
```

This script will install the library, called *pimglow* and copy the examples in this repository to `~/Pimoroni/piglow`

## Backwards Compatibility

The Pimglow Python library is designed to coincide with Jason's PiGlow library found here: https://github.com/Boeeerb/PiGlow

It's compatible with the examples, and we've ported some over to show you how it's done.

## Using PiGlow

To use the pimglow library, you'll probably want to start by importing it:

```python
import pimglow as piglow
```

Now, you can turn some LEDs on:

```python
piglow.red(64)
```

Nothing will happen yet, you've got to update PiGlow with your changes. Why? Because it's quicker! If you're setting up a pattern it costs time and resources to redraw every step of that setup to the PiGlow, so we don't do that. Instead you need to call `show` like so:

```python
piglow.show()
```

##Function Reference

### Colours
* `white( value from 0 to 255 )`
* `blue( value from 0 to 255 )`
* `green( value from 0 to 255 )`
* `yellow( value from 0 to 255 )`
* `orange( value from 0 to 255 )`
* `red( value from 0 to 255 )`

### Arm, Spoke, Leg, they're all the same thing!

`arm( index from 0 to 2, value from 0 to 255 )`

### Multiple LEDs in various different ways

The `set` method accepts a list of LEDs, a list of values, or a single LED or value, or any permutation therein:

`set(0, 255)` - sets LED 0 to full brightness

`set([1,3,5,7,9,11,13,15,17],255)` - sets all odd LEDs to full brightness

`set(0,[50,50,50])` - let the 3 LEDs starting at index 0 to 50 brightness
