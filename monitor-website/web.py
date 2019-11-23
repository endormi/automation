"""

author: @endormi

Automated website monitoring for exceptions
if there is an exception it sends an email and plays a sound (remember to turn down your volume)

"""

import requests
from playsound import playsound
import smtplib


url = ''
PORT = 587
Your_Email = 'example@company.com'

"""
Get your password from:
https://myaccount.google.com/apppasswords
"""
Your_Password = 'password'


req = requests.get(url, timeout=1)
req.raise_for_status()

if req.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', PORT) as send__mail:
        send__mail.starttls()

        send__mail.login(Your_Email, Your_Password)

        sub = 'Your site is down!'
        body = 'Restart the server and make sure it is running.'
        message = f'Subject: {sub} \n\n {body}'

        send__mail.sendmail(Your_Email, Your_Email, message)
        print("Email sent!")

    playsound('volume_warning.wav')
else:
    print("Works correctly")
