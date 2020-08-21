"""

author: @endormi

Keyboard abbreviations (type @.. and then press space)

"""

import keyboard

keyboard.add_abbreviation('@email', 'your.email@example.com')
keyboard.add_abbreviation('@gh', 'your_github')
keyboard.add_abbreviation('@t', 'your_twitter')
keyboard.wait('esc')
