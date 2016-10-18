import csv
import os
import xlsxwriter


from src.processing.convert_excel import xlsx2csv


def test_xlsx2csv():
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Hello, world')
    worksheet.write('A2', 'Second row')
    worksheet.write('B2', 'Second Column')
    workbook.close()

    xlsx2csv('hello.xlsx', 'Sheet1', 'hello.csv')
    with open('hello.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        entries = []
        for row in reader:
            entries.append(row)
    os.remove('hello.csv')
    os.remove('hello.xlsx')
    assert len(entries) == 2
    assert entries[0][0] == 'Hello, world'
    assert entries[1][0] == 'Second row'
    assert entries[1][1] == "Second Column"
