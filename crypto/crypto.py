"""

author: @endormi

Automated notifier when specified CryptoCurrency price changes
It sends a notification to sms (use whatever you wish) using ifttt app

"""

import requests
from datetime import datetime
import time

"""
https://api.coinmarketcap.com/v1/ticker/bitcoin/
https://api.coinmarketcap.com/v1/ticker/litecoin/
etc.
"""

api = ''

"""
Create your ifttt applet and follow the webhooks documentation
"""
ifttt_url = ''


def latest():
    response = requests.get(api)
    res = response.json()
    # check res: print(res[0]['price_usd'])
    return float(res[0]['price_usd'])


def ifttt(event, value):
    val = {'value1': value}
    ifttt_e = ifttt_url.format(event)
    # check request: print(requests.post(ifttt_e, json=val))
    requests.post(ifttt_e, json=val)


def format_crypto(crypto):

    row = []

    for crypto_price in crypto:
        """
        Format the notification to create rows
        including date and price (date is formatted to use day, month, year, hour and minutes)
        """
        date = crypto_price['date'].strftime('%d.%m.%Y %H:%M')
        price = crypto_price['price']

        a_row = '{}: ${}'.format(date, price)
        row.append(a_row)

    return '<br>'.join(row)


def main():

    crypto = []

    while True:
        price = latest()
        date = datetime.now()
        crypto.append({'date': date, 'price': price})

        """
        When 3 price changes are in specied cryptocurrency,
        ifttt sends a notification
        """
        if len(crypto) == 3:
            ifttt('applet_name', format_crypto(crypto))

        # Reset crypto
        crypto = []

        time.sleep(500)


if __name__ == '__main__':
    main()
