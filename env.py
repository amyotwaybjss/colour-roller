# this sheet will create our 'settings', load in sheet, get sheet list, store vars

import openpyxl as xl

wb = xl.load_workbook('colours2.xlsx')

sheet_list = wb.sheetnames
# list of active sheet names


def print_env_message():
    print("This is from env")

# This function is added as without a function, the import statement does not work correctly;
# Pulls in everything rather than just the respective variables.


print(sheet_list)
