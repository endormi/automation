"""

author: @endormi

Move cursor every 10 seconds

"""

import pyautogui
import random
import time


def countdown_timer(start, end):
    for i in range(start, end, 1):
        time.sleep(1)
        print(i, end="\r")


def main():
    while True:
        pyautogui.moveTo(random.randint(100, 500), random.randint(10, 50), duration=1)
        countdown_timer(1, 10)


if __name__ == '__main__':
    main()
