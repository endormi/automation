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

except requests.exceptions.HTTPError as http_err:
    print("HTTP Error: ", http_err)
    playsound('volume_warning.wav')

except requests.exceptions.ConnectionError as connect_err:
    print("Error Connecting: ", connect_err)
    playsound('volume_warning.wav')

except requests.exceptions.Timeout as time_err:
    print("Timeout Error: ", time_err)
    playsound('volume_warning.wav')

except requests.exceptions.TooManyRedirects as err:
    print("Too many redirects: ", err)
    playsound('volume_warning.wav')

except requests.exceptions.RequestException as request_err:
    print("General error: ", request_err)
    playsound('volume_warning.wav')
except KeyboardInterrupt:
    print("Someone closed the program")
