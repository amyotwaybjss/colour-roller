# Normal colour roll selects a column first, then picks a colour.
# After that, it selects either the same or a different column, then picks another colour.
# With colour priority it should give each colour a chance of being selected.
# Colour is selected, then the program looks up its column.
# It should then either pick something from the same or a different column.

from env import (wb, sheet_list, new_line, status)
from user_settings import sheet_category
from mode_select import category_list, active
import random as ran

shuffle = "match"

# Func start

sheet_name = wb['watercolours']
max_col = sheet_name.max_column
max_row = sheet_name.max_row

if shuffle == "random":
    shuffle = ran.choice(["match", "mix"])

match = max_col == 1 or shuffle in ("match", "single")  # result binary TRUE/FALSE

choice = None
header = None
choose_col = 0
choose_row = 0

while choice is None:
    choose_col, choose_row = ran.randint(1, max_col), ran.randint(2, max_row)
    choice = sheet_name.cell(choose_row, choose_col).value
    header = sheet_name.cell(1, choose_col).value

random_choice = f'{header}: {choice}'
print(random_choice)

# print(choose_row)
# print(choose_col)

# col_select1 = col_select2 = choose_col

# if single, then done
# if match, then pick randomly from same col as usual.
# if not match, then run process again.


# print(col_select1)
# print(col_select2)

# list priority, picks a list, then picks from that list
# colour priority, picks a colour from all lists, then picks another based on that list

