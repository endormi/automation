"""

author: @endormi

Python program process time

"""

import os
import psutil


process = psutil.Process(os.getpid())
print('Process time: ' + str(process.memory_percent()))
