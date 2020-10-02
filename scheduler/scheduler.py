"""

author: @endormi

Automated job schedules

"""

import schedule
import webbrowser
import os
import sys
import ctypes
import time
from playsound import playsound


def run():
    print('Running scheduler...')


def certain_show():
    playsound('sound.wav')
    print('Show ... is on!')


def open_email():
    # If you need to login everytime, you can use my selenium-testing templates to figure it out
    print('Opening email..')
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')


def shutdown():
    if sys.platform == 'win32':
        user32 = ctypes.WinDLL('user32')
        user32.ExitWindowsEx(0x00000008, 0x00000000)
    else:
        os.system('sudo shutdown now')


# This is just a random time I added
schedule.every().monday.at("20:00").do(certain_show)
schedule.every().tuesday.at("20:00").do(certain_show)

schedule.every(30).minutes.do(run)

schedule.every().day.at("08:00").do(open_email)
schedule.every().day.at("23:00").do(shutdown)

"""
schedule.every().minute.at(":30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().hour.do(job)
"""

while True:
    schedule.run_pending()
    time.sleep(1)
