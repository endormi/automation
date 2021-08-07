"""

author: @endormi

Record keyboard until ctrl-z is pressed

"""

import keyboard


event = keyboard.record(until='ctrl + z')
keyboard.play(event, speed_factor=1)
print(event)
