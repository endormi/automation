"""

author: @endormi

Count the mortgage payment

"""

loan = float(input('Enter the loan amount: '))
years = float(input('How many years will you have the loan? ')) * 12
interest = float(input('Enter the interest rate (%): ')) / 100 / 12

mortgage = loan * (interest * (1 + interest) ** years) / ((1 + interest) ** years - 1)

print('The monthly mortgage payment is {0:.2f} '.format(mortgage))
