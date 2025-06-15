import time
import board
import digitalio
import neopixel

np_power = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
np_power.switch_to_output(value=True)

np = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    np[0] = (0, 50, 0)
    time.sleep(3)
    np[0] = (0, 0, 0)
    time.sleep(3)
    np_power.switch_to_output(value=False)
    time.sleep(3)
    np_power.switch_to_output(value=True)
