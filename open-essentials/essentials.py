"""

author: @endormi

Experimental automation that opens all of the essentials
for development such as websites, tools and editor

"""

import pyautogui
import webbrowser
import time

# print(pyautogui.position())

webbrowser.open('chrome')
# webbrowser.open('mozilla')
# webbrowser.open('safari')

pyautogui.moveTo(x=414, y=51, duration=1)
pyautogui.click(x=414, y=51)
pyautogui.typewrite("github.com")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=414, y=51)
pyautogui.typewrite("stackoverflow.com")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=414, y=51)
pyautogui.typewrite("gmail.com")
pyautogui.typewrite(["enter"])
pyautogui.click(x=414, y=51)

# pyautogui.hotkey("ctrl", "t")
# pyautogui.typewrite("wtf is going on?!?!")


"""
My spotify, powershell and vscode (vscode is last because of the hotkey's) are on these positions
Checking cursor position: print(pyautogui.position())
"""

pyautogui.click(x=271, y=1067)
pyautogui.click(x=427, y=1067)
pyautogui.click(x=523, y=1072)

"""
If you're wondering why I have two hotkey's for vscode, I always open a new window and then open a folder, just a habit of mine
** If your computer is not that fast, add more time to (time.sleep) **
"""

time.sleep(2)

pyautogui.hotkey("ctrl", "shift", "n")

time.sleep(2)

pyautogui.hotkey("ctrl", "o")
