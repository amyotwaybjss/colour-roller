# this sheet will create our 'settings', load in sheet, get sheet list, store vars

import openpyxl as xl
import os.path as path
from data_clean import data_clean
from user_settings import wb_name, force_refresh

try:
    wb_input = xl.load_workbook(f'{wb_name}.xlsx')
except FileNotFoundError:
    print('Error: Named sheet has not been found, please check the file and re-run.')
    quit()
except PermissionError:
    print('Error: Unable to access file, please check file is closed and re-run.')
    quit()


def clean_exists(load, name):
    if path.isfile(f'./{name}_cleaned.xlsx') is False or force_refresh is True:
        data_clean(load, name)


clean_exists(wb_input, wb_name)

wb = xl.load_workbook(f'{wb_name}_cleaned.xlsx')

sheet_list = wb.sheetnames

new_line = "\n"


def status(mode, sheets):
    stat = f'Mode: {mode}{new_line}Active Sheets: {sheets}'
    return stat

# Note that without a function, importing variables does not work correctly;
# Everything is pulled in rather than just the respective variables.
