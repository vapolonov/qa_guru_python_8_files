import xlrd

book = xlrd.open_workbook('resources/file_example_50.xls')
print(book.nsheets)  # количество листов 1
print(book.sheet_names())  # названия листов ['Sheet1']
sheet = book.sheet_by_index(0)
print(f'Количество столбцов {sheet.ncols}')  # Количество столбцов 8
print(f'Количество строк {sheet.nrows}')  # Количество строк 51
print(f'Ячейка 9:1 = {sheet.cell_value(rowx=9, colx=1)}')  # Ячейка 9:1 = Vincenza (индексы с 0)
for rx in range(sheet.nrows):
    print(*sheet.row(rx))

