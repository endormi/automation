"""

author: @endormi

Automated excel graphs

"""

import pandas
import matplotlib.pyplot as plt


df = pandas.read_excel('filename.xslx')
val = df[['Expenses', 'Income']]

xy = val.plot.bar(x='Expenses', y='Income')
plt.show()
