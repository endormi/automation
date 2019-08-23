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


for mv in move_file:
    # filetypes
    if mv.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        shutil.move(mv, images)
    if mv.endswith(('.mp3', '.wav', '.mid')):
        shutil.move(mv, audio)
    if mv.endswith(('.pdf', '.doc', '.docx', '.docxml')):
        shutil.move(mv, pdf_doc)
    if mv.endswith(('.txt', '.text', '.note')):
        shutil.move(mv, texts)
    if mv.endswith(('.mp4', '.avi', '.mov', '.vmw', '.flv')):
        shutil.move(mv, videos)
    if mv.endswith(('.zip', '.rar', '.tar', '.7z')):
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
print("Finished moving files!")
