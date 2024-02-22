import random as ran


def roller(load, sheet):
    colours = load[sheet]
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
        result = f'{header}: {first_col} only'
    else:
        result = f'{header}: {first_col} and {second_col}'

    return result
