"""

author: @endormi

Read and pressed key (is_pressed requires you to actually hold it)

"""

import keyboard

while True:
    if keyboard.read_key() == 'c':
        print('Pressed C')
        break
    elif keyboard.read_key() == 'esc':
        print('Closing program..')
        break
    elif keyboard.is_pressed('w'):
        print('Pressed W')
        break
