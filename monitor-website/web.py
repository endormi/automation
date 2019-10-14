"""

author: @endormi

Automated website monitoring for exceptions
if there is an exception it plays a sound (remember to turn down your volume)

"""

import requests
from playsound import playsound


url = ''

try:
    req = requests.get(url, timeout=1)
    req.raise_for_status()

    if req.status_code == 200:
        print('Success!')

except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)
    playsound('volume_warning.wav')

except requests.exceptions.ConnectionError as err:
    print("Error Connecting:", err)
    playsound('volume_warning.wav')

except requests.exceptions.Timeout as err:
    print("Timeout Error:", err)
    playsound('volume_warning.wav')

except requests.exceptions.TooManyRedirects as err:
    print("Too many redirects:", err)
    playsound('volume_warning.wav')

except requests.exceptions.RequestException as err:
    print(err)
    playsound('volume_warning.wav')
