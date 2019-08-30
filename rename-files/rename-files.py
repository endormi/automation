"""

author: @endormi

Automated file renaming
Currently works with title and num, but change it to your own preference

"""

import os
import time


PATH = r'folder/for/files'

os.chdir(PATH)


for files in os.listdir():
    file, extension = os.path.splitext(files)

    """
    This is totally up to your file format
    """
    title, num = file.split('-')
    # print(file.split('-'))

    title = title.strip()
    num = num.strip()[0:].zfill(3)

    rename_file = '{}-{}{}'.format(num, title, extension)

    # Automation
    print('Renaming file: ')
    print('{}-{}{}'.format(num, title, extension))

    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)

    os.rename(files, rename_file)
