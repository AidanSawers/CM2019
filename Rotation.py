from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin13, 12)

while True:

    for i in range(0, len(np)):
        np[i] = (60, 0, 0)
        for j in range(0, len(np)):
            if not (i == j):
                np[j] = (0, 0, 60)
            np.show()
        sleep(500)