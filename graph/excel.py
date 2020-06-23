"""

author: @endormi

Automated excel graphs

"""

import pandas
import matplotlib.pyplot as plt


df = pandas.read_excel('filename.xslx')
val = df[['Month', 'Income']]

xy = val.plot.bar(x='Month', y='Income')
plt.show()
