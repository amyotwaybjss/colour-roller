# import openpyxl as xl
import random as ran
from env import wb
# why is this importing everything from env?

# wb = xl.load_workbook('colours2.xlsx')
# moved to env

# sheet = wb['markers']
# this is now dynamic


def roller(sheet):
    colours = wb[sheet]
    max_col = colours.max_column

    col_select = ran.randint(1, max_col)

    selection = []
    header = colours.cell(1, col_select).value

    for rows in range(2, colours.max_row+1):
        if colours.cell(rows, col_select).value is None:
            pass
        else:
            value = colours.cell(rows, col_select).value
            selection.append(value)

    first_col = ran.choice(selection)
    second_col = ran.choice(selection)

    if first_col == second_col:
        print(f'{header}: {first_col} only')
    else:
        print(f'{header}: {first_col} and {second_col}')


# roller('watercolours')
