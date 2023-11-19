import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open('csv_file.csv', 'r') as csv_file:
    file_reader = csv.DictReader(csv_file)

    for i in range(2, 8):
        ws.cell(row=1, column=i).value = f'Person {i - 1}'

    res_dict = {'id': [], 'name': [], 'phone': []}

    for row in file_reader:
        for key in row:
            if key in res_dict:
                res_dict[key].append(row[key])

    for key in res_dict:
        ws.append([key] + res_dict[key])

    wb.save('excel_file.xlsx')

workbook = openpyxl.load_workbook('excel_file.xlsx')

for row in workbook.active:
    for cell in row:
        print(str(cell.value).ljust(10), end=' ')
    print()
