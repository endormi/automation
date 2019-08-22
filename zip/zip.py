"""

author: @endormi

Minimal automation compressing files

"""

from zipfile import ZipFile

zip = ZipFile('name_of_zip_file', 'w')
zip.write('path/to/file', compress_type=ZipFile.ZIP_DEFLATED)

try:
    print("Compressing a file")
finally:
    zip.close()
