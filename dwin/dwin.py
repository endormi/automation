"""

author: @endormi

Automated terminal running and commands, not that useful (since it would obvs be better to use sh or bat)
but decided to add since it's a good addition :)

This script starts a new Django project.

"""

import pyautogui
import time


terminal = ''
dir = ''
folder = ''
project = ''
new = ''


pyautogui.press('win')
pyautogui.typewrite(terminal)
pyautogui.typewrite(['enter'])
pyautogui.typewrite('cd ./' + dir + ' &&' + ' mkdir ' + folder + ' && ' + 'cd ' + folder)
pyautogui.typewrite(['enter'])
pyautogui.typewrite('django-admin.py startproject ' + project)
pyautogui.typewrite(['enter'])
pyautogui.typewrite('cd ' + project + ' &&' + ' python manage.py startapp ' + new)
pyautogui.typewrite(['enter'])
time.sleep(1)
pyautogui.typewrite('python manage.py migrate')
pyautogui.typewrite(['enter'])
pyautogui.typewrite('python manage.py runserver')
pyautogui.typewrite(['enter'])
