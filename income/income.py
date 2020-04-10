"""

author: @endormi

Income tracker
Automatically adds to excel

"""

import xlsxwriter

wb = xlsxwriter.Workbook('filename.xlsx', {'strings_to_numbers': True})
wsb = wb.add_worksheet(name='Income')
bold = wb.add_format({'bold': True})

row = 2
col = 0

wsb.write('A1', 'Income', bold)
wsb.write('A2', 'Date:', bold)
wsb.write('B2', 'Type of income:', bold)
wsb.write('C2', 'Amount of income:', bold)
wsb.write('D2', 'Total:', bold)

currency_format = wb.add_format({'num_format': '# ##0.00 €'})

income = (
    ['01.01.2020', 'type1', '1000'],
    ['01.01.2020', 'type2', '1000'],
    ['01.01.2020', 'type3', '1000'],
    ['01.01.2020', 'type4', '1000'],
    ['01.01.2020', 'type4', '1000'],
    ['01.01.2020', 'type5', '1000'],
)

for i, r, c in (income):
    wsb.write(row, col, i)
    wsb.write(row, col + 1, r)
    wsb.write(row, col + 2, c)
    row += 1

wsb.write_formula("D3", "=SUM(C3:C7)", currency_format)

wb.close()
