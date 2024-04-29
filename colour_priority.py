# Normal colour roll selects a column first, then picks a colour.
# After that, it selects either the same or a different column, then picks another colour.
# With colour priority it should give each colour a chance of being selected.
# Colour is selected, then the program looks up its column.
# It should then either pick something from the same or a different column.

from env import (wb, sheet_list, new_line, status)
from user_settings import sheet_category
from mode_select import category_list, active
import random as ran

shuffle = "match"  # option are random, match, mix, single

# Func start

sheet_name = wb['watercolours']
max_col = sheet_name.max_column
max_row = sheet_name.max_row

all_columns = list(range(1, max_col+1))

if shuffle == "random":
    shuffle = ran.choice(["match", "mix"])

matching = max_col == 1 or shuffle in ("match", "single")  # result binary TRUE/FALSE

pick = []
headers = []

for picks in range(1, 3):  # Python goes from a to b-1

    choice = None
    header = None
    choose_col = ''

    while choice is None:
        choose_col, choose_row = ran.choice(all_columns), ran.randint(2, max_row)
        choice = sheet_name.cell(choose_row, choose_col).value
        header = sheet_name.cell(1, choose_col).value

    if matching:
        all_columns = [choose_col]
    else:
        all_columns.remove(choose_col)

    random_choice = f'{header}: {choice}'

    if random_choice in pick or (len(pick) == 1 and shuffle == "single"):
        pass
    else:
        pick.append(random_choice)
        if header in headers:
            pass
        else:
            headers.append(header)

# print(pick)

first = pick[0]

if (len(pick)) == 1:
    result = f'{first} only'
else:
    if (len(headers)) == 1:
        second = pick[1].split(' ')[1]
    else:
        second = pick[1]
    result = f'{first} and {second}'

print(result)

# if single, then done
# if match, then pick randomly from same col as usual.
# if not match, then run process again.
