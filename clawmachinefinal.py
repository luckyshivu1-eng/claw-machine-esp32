from machine import Pin
from servo import Servo
import neopixel
import time

#servos
servo1 = Servo(Pin(18))
servo2 = Servo(Pin(19))

btn1_right = Pin(14, Pin.IN, Pin.PULL_UP)
btn1_left  = Pin(27, Pin.IN, Pin.PULL_UP)
btn2_up    = Pin(26, Pin.IN, Pin.PULL_UP)
btn2_down  = Pin(25, Pin.IN, Pin.PULL_UP)

angle1 = 90
angle2 = 90
servo1.write_angle(angle1)
servo2.write_angle(angle2)

p1r = p1l = p2u = p2d = 1

# neopixels
NUM_LEDS = 16
np = neopixel.NeoPixel(Pin(5), NUM_LEDS)

def ring_pink():
    for i in range(NUM_LEDS):
        np[i] = (255, 20, 147)
    np.write()

def ring_green():
    for i in range(NUM_LEDS):
        np[i] = (0, 255, 0)
    np.write()

ring_pink()

#main loop
while True:

    c1r = btn1_right.value()
    c1l = btn1_left.value()
    c2u = btn2_up.value()
    c2d = btn2_down.value()

    # servo 1
    if p1r == 1 and c1r == 0:
        if angle1 <= 170:
            angle1 += 10
            servo1.write_angle(angle1)

    if p1l == 1 and c1l == 0:
        if angle1 >= 10:
            angle1 -= 10
            servo1.write_angle(angle1)

    # servo2
    if p2u == 1 and c2u == 0:
        if angle2 <= 170:
            angle2 += 10
            servo2.write_angle(angle2)

    if p2d == 1 and c2d == 0:
        if angle2 >= 10:
            angle2 -= 10
            servo2.write_angle(angle2)
#neopixel colour part
    if 10 <= angle2 <= 40:
        ring_green()
    else:
        ring_pink()

    p1r = c1r
    p1l = c1l
    p2u = c2u
    p2d = c2d

    time.sleep(0.01)