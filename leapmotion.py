"""
THIS FILE REQUIRES THE LEAP DEVELOPER LIBRARIES TO BE PRESENT IN THE SAME DIRECTORY
This is the backend to the Leap Motion interface to Minecraft.
"""

import Leap
import time
from pykeyboard import PyKeyboard
k = PyKeyboard()

c = Leap.Controller()
c.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)


while True:
    time.sleep(0.1)
    f = c.frame()
    pos = f.hands[0].stabilized_palm_position
    if pos.x > 60:
        k.press_key('d')
    elif pos.x < -60:
        k.press_key('a')
    else:
        k.release_key('d')
        k.release_key('a')

    if pos.z < -40:
        k.press_key('w')
    elif pos.z > 40:
        k.press_key('s')
    else:
        k.release_key('w')
        k.release_key('s')


    if pos.z < -80:
        k.press_key('z')
    else:
        k.release_key('z')

    if pos.y > 250:
        k.press_key('c')
    elif pos.y < 80 and pos.y > 0:
        k.press_key('x')
    else:
        k.release_key('x')
        k.release_key('c')
