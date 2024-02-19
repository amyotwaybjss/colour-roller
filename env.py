# this sheet will create our 'settings', load in sheet, get sheet list, store vars

import openpyxl as xl

wb = xl.load_workbook('colours2.xlsx')

sheet_list = wb.sheetnames
# list of active sheet names

new_line = "\n"


def status(mode, sheets):
    stat = f'Mode: {mode}{new_line}Active Sheets: {sheets}'
    return stat

# Note that without a function, importing variables does not work correctly;
# Pulls in everything rather than just the respective variables.


sheet_category = {
    "pii": ["personal", "private", "nonexistent"],
    "sensitive": ["private", "business1", "business2", "business3"],
    # "test": ["private"]
}

# this creates a dictionary for sheet category
# permissions controlled in mode_select
# note that the brackets are essential!
