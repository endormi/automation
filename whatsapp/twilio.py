"""

author: @endormi

Automated text sender for Whatsapp with Twilio

"""

from twilio.rest import Client


client = Client()

from_number = 'whatsapp:000'

contacts = {'add contact here': 'number'}


for key, value in contacts.items():
    send_messages = client.messages.create(
                                           body='Hello world',
                                           image='link/to/image',
                                           from_=from_number,
                                           to='whatsapp:' + value,)

    print(send_messages.sid)
