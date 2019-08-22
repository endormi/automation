"""

author: @endormi

Minimal automation compressing folders

"""

import os
from zipfile import ZipFile


def folder__path(directory):
    folder_path = []
    for root, directories, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            folder_path.append(path)
    return folder_path


def main():
    directory = 'path/to/directory'
    folder_path = folder__path(directory)

    for file in folder_path:
        print(file)

    zip = ZipFile(directory + '.zip', 'w')
    for folder in folder_path:
        zip.write(folder)

    print(directory + " : is compressed!")
    zip.close()


if __name__ == '__main__':
    main()
