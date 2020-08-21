"""

author: @endormi

Spawn a dragon in Skyrim every 5 seconds,
this is just a useless and random python program

"""

import pyautogui
import time


class enemy:
    dragon = '0200c5f5'
    other = ''


while True:
    time.sleep(1)
    pyautogui.press('~')
    pyautogui.typewrite('player.placeatme ' + enemy.dragon + ' 1')
    pyautogui.typewrite(['enter'])
    time.sleep(4)
