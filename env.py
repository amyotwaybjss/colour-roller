import openpyxl as xl

wb = xl.load_workbook('colours2.xlsx')

sheet_list = wb.sheetnames


def print_env_message():
    print("This is from env")

# This function is added as without a function, the import statement does not work correctly;
# Pulls in everything rather than just the respective variables.

# this sheet will create our 'settings', load in sheet etc.
# aka which sheets are in current spreadsheet and put them in a list.
# also probably load vars
