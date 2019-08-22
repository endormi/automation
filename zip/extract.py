"""

author: @endormi

Minimal automation extracting .zip files

"""

from zipfile import ZipFile

zip = ZipFile('path/to/file', 'r')
zip.extractall()

try:
    print("Extracting .zip file")
finally:
    zip.close()
