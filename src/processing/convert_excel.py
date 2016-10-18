# -*- coding: utf-8 -*-
import csv
import xlrd


def xlsx2csv(workbook_path, sheetname, csv_path):
    wb = xlrd.open_workbook(workbook_path)
    sh = wb.sheet_by_name(sheetname)
    csv_file = open(csv_path, 'w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    csv_file.close()
