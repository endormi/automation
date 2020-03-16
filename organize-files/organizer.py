"""

author: @endormi

Automated organizer for images, audio, texts, videos and compressed files
and moves them inside specified folders

"""

import os
import shutil
import time
from pyfiglet import figlet_format
from termcolor import cprint


logo = 'Organizer'


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''
Automated organizer for images, audio, texts, videos, compressed files
 and moves them inside specified folders.\n''' + color.END


PATH = r'folder/to/organize'

images = r'destination/for/images'
audio = r'destination/for/audio'
docs = r'destination/for/docs'
texts = r'destination/for/texts'
videos = r'destination/for/videos'
compressed_files = r'destination/for/compressed'

os.chdir(PATH)
move_file = os.listdir(PATH)


def organize():
    print("Organizing files!")

    for mv in move_file:
        # filetypes
        if mv.endswith(('png', 'jpg', 'jpeg', 'gif', 'ico', 'svg')):
            if not os.path.exists(f"{images}"):
                os.mkdir(f"{images}")
            shutil.move(mv, images)
        if mv.endswith(('mp3', 'wav', 'mid', 'midi', 'ogg')):
            if not os.path.exists(f"{audio}"):
                os.mkdir(f"{audio}")
            shutil.move(mv, audio)
        if mv.endswith(('pdf', 'doc', 'docx', 'docxml')):
            if not os.path.exists(f"{docs}"):
                os.mkdir(f"{docs}")
            shutil.move(mv, docs)
        if mv.endswith(('txt', 'text', 'note', 'rtf')):
            if not os.path.exists(f"{texts}"):
                os.mkdir(f"{texts}")
            shutil.move(mv, texts)
        if mv.endswith(('mp4', 'avi', 'mov', 'vmw', 'flv', 'mpeg', 'mpg')):
            if not os.path.exists(f"{videos}"):
                os.mkdir(f"{videos}")
            shutil.move(mv, videos)
        if mv.endswith(('zip', 'rar', 'tar', '7z', 'pkg')):
            if not os.path.exists(f"{compressed_files}"):
                os.mkdir(f"{compressed_files}")
            shutil.move(mv, compressed_files)

    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Finished organizing files!")


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info + "\n")

    if len(move_file) > 0:
        print(f"Found {len(move_file)} file(s). \n")
        organize()

    else:
        print("No files found!")
        print("Check your path: " + PATH)


if __name__ == '__main__':
    main()
