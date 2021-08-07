"""

author: @endormi

Small script to check computer memory (total, available, usage, used and free)

"""

import psutil


file = 'file.txt'

mem = psutil.virtual_memory()

print(str(mem) + '\n')
print('Total memory: ' + str(mem.total))
print('Available memory: ' + str(mem.available))
print('Memory usage: ' + str(mem.percent))
print('Used memory: ' + str(mem.used))
print('Free memory: ' + str(mem.free))

with open(file, 'a') as i:
    i.write('Total memory: ' + str(mem.total) + '\n')
    i.write('Available memory: ' + str(mem.available) + '\n')
    i.write('Memory usage: ' + str(mem.percent) + '\n')
    i.write('Used memory: ' + str(mem.used) + '\n')
    i.write('Free memory: ' + str(mem.free) + '\n')
    i.write('\n')

    print('\nWrote results to' + file)
