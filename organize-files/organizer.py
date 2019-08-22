"""

author: @endormi

Automated organizer for images, audio, texts, videos and compressed files
and moves them inside folders e.g. images

"""

import os
import shutil
import time

PATH = r'folder/to/organize'

images = r'destination/for/images'
audio = r'destination/for/audio'
pdf_doc = r'destination/for/PDF_Doc'
texts = r'destination/for/texts'
videos = r'destination/for/videos'
compressed_files = r'destination/for/compressed'

os.chdir(PATH)
move_file = os.listdir(PATH)

try:
    for mv in move_file:
        # filetypes
        if mv.endswith('.png'):
            shutil.move(mv, images)
        if mv.endswith('.jpg'):
            shutil.move(mv, images)
        if mv.endswith('.jpeg'):
            shutil.move(mv, images)
        if mv.endswith('.gif'):
            shutil.move(mv, images)
        if mv.endswith('.mp3'):
            shutil.move(mv, audio)
        if mv.endswith('.wav'):
            shutil.move(mv, audio)
        if mv.endswith('.mid'):
            shutil.move(mv, audio)
        if mv.endswith('.pdf'):
            shutil.move(mv, pdf_doc)
        if mv.endswith('.doc'):
            shutil.move(mv, pdf_doc)
        if mv.endswith('.docx'):
            shutil.move(mv, pdf_doc)
        if mv.endswith('.docxml'):
            shutil.move(mv, pdf_doc)
        if mv.endswith('.txt'):
            shutil.move(mv, texts)
        if mv.endswith('.text'):
            shutil.move(mv, texts)
        if mv.endswith('.note'):
            shutil.move(mv, texts)
        if mv.endswith('.mp4'):
            shutil.move(mv, videos)
        if mv.endswith('.avi'):
            shutil.move(mv, videos)
        if mv.endswith('.mov'):
            shutil.move(mv, videos)
        if mv.endswith('.wmw'):
            shutil.move(mv, videos)
        if mv.endswith('.flv'):
            shutil.move(mv, videos)
        if mv.endswith('.zip'):
            shutil.move(mv, compressed_files)
        if mv.endswith('.rar'):
            shutil.move(mv, compressed_files)
        if mv.endswith('.tar'):
            shutil.move(mv, compressed_files)
        if mv.endswith('.7z'):
            shutil.move(mv, compressed_files)

    print("Organizing files!")

    # Animation
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
finally:
    print("Finished moving files!")
