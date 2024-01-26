import openpyxl as xl

wb = xl.load_workbook('colours2.xlsx')

sheet_list = wb.sheetnames

# print(sheet_list)

# this sheet will create our 'settings', load in sheet etc.
# aka which sheets are in current spreadsheet and put them in a list.
# also probably load vars
