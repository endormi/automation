"""

author: @endormi

Experimental automation that opens all of the essentials
for development such as websites, tools and editor

"""

import pyautogui
import webbrowser
import time

webbrowser.open('chrome')
"""
webbrowser.open('mozilla')
webbrowser.open('safari')
"""

# Checking cursor position: print(pyautogui.position())
pyautogui.moveTo(414, 51, duration=1)
pyautogui.click(414, 51)
pyautogui.typewrite("github.com")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(414, 51)
pyautogui.typewrite("stackoverflow.com")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(414, 51)
pyautogui.typewrite("gmail.com")
pyautogui.typewrite(["enter"])
pyautogui.click(414, 51)

"""
Opens spotify, powershell and vscode on my computer
"""

pyautogui.click(271, 1067)
pyautogui.click(427, 1067)
pyautogui.click(523, 1072)


# ** If your computer is not that fast, add more time to (time.sleep) **

time.sleep(1)
pyautogui.hotkey("ctrl", "shift", "n")
time.sleep(1)
pyautogui.hotkey("ctrl", "o")
