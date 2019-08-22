"""

author: @endormi

Minimal automation extracting .zip files

"""

from zipfile import ZipFile


try:
    zip = ZipFile('path/to/file', 'r')
    zip.extractall()
    print("Extracting .zip file")
finally:
    zip.close()
