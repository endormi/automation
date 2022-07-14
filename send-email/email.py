"""

author: @endormi

Automated email sender (uses gmail's port)
subject, content and image attachments

"""

import smtplib
from email.message import EmailMessage
import imghdr


PORT = 587

Your_Email = 'example@company.com'

"""
Get your password from:
https://myaccount.google.com/apppasswords
"""
Your_Password = 'password'

receiver = input("Person receiving the email: ")
subject = input("Message subject: ")
content = input("Message content: ")

with smtplib.SMTP('smtp.gmail.com', PORT) as send__mail:
    send__mail.starttls()
    send__mail.login(Your_Email, Your_Password)

    message = EmailMessage()
    message['From'] = Your_Email
    message['To'] = receiver
    message['subject'] = subject
    message.set_content(content)

    """ Uncomment if you wish to send image attachments

    with open('image/file', 'rb') as image_attachment:
        img = image_attachment.read()
        img_type = imghdr.what(image_attachment.name)
    message.add_attachment(img, maintype='image', subtype=img_type)
    """

    send__mail.send_message(message)

    print("Email sent!")
