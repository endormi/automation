"""

author: @endormi

Minimal automation compressing files
**NOTE: This should work with .7z files**

"""

from zipfile import ZipFile


try:
    zip = ZipFile('name_of_zip_file', 'w')
    zip.write('path/to/file', compress_type=ZipFile.ZIP_DEFLATED)
    print("Compressing a file")
finally:
    zip.close()
