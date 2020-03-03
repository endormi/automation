"""

author: @endormi

Automated boring csv parser with a tab delimiter

"""

import csv


with open('csv_file', 'r') as file:
    read = csv.reader(file)

    with open('csv_file', 'w') as f:
        write = csv.writer(f, delimiter='\t')

        for list in read:
            write.writerow(list)
