"""

author: @endormi

Keyboard hotkey

"""

import keyboard

keyboard.add_hotkey('ctrl + z', print, args=('this is', 'a hotkey'))
keyboard.wait('esc')
