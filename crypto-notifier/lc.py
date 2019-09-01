"""

author: @endormi

Automated notifier when LiteCoin price changes,
It sends a notification to sms (use whatever you wish) using ifttt app

"""

import requests
from datetime import datetime
import time


url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'

"""
Create your ifttt applet and follow the webhooks documentation
"""
ifttt_url = ''


lc_ts = 1000


def latest_price():
    response = requests.get(url)
    res = response.json()
    # check res: print(res[0]['price_usd'])
    return float(res[0]['price_usd'])


def ifttt_hook(event, value):
    val = {'value1': value}
    ifttt_e = ifttt_url.format(event)
    # check request: print(requests.post(ifttt_e, json=val))
    requests.post(ifttt_e, json=val)


def format_lc(lc):

    rows = []

    for __lc__price in lc:
        """
        Format the notification to create rows
        including date and price (date is formatted to use day, month, year, hour and minutes)
        """
        date = __lc__price['date'].strftime('%d.%m.%Y %H:%M')
        price = __lc__price['price']

        a_row = '{}: ${}'.format(date, price)
        rows.append(a_row)

    return '<br>'.join(rows)


def main():

    lc = []

    while True:
        price = latest_price()
        date = datetime.now()
        lc.append({'date': date, 'price': price})

        """
        When 3 items is in lc,
        it sends a notification
        """
        if len(lc) == 3:
            ifttt_hook('lc_price', format_lc(lc))

        # Reset lc
        lc = []

        time.sleep(500)


if __name__ == '__main__':
    main()
