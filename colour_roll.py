import random as ran


def roller(workbook, sheet, setting):  # e.g. roller(wb, watercolours)
    sheet_name = workbook[sheet]
    max_col = sheet_name.max_column

    match = max_col == 1 or setting == 'match'

    # select a random column from chosen sheet

    col_select1 = ran.randint(1, max_col)
    col_select2 = col_select1

    # if more than one column, set col_select2 to be different column

    if not match:
        while col_select2 == col_select1:
            col_select2 = ran.randint(1, max_col)

    pick = []
    headers = []

# loop through the two chosen columns and select random options

    for selected in [col_select1, col_select2]:

        header = sheet_name.cell(1, selected).value

        selection = []

        for rows in range(2, sheet_name.max_row+1):
            if sheet_name.cell(rows, selected).value is None:
                pass
            else:
                value = sheet_name.cell(rows, selected).value
                selection.append(value)

        random_choice = f'{header}: {ran.choice(selection)}'

        if random_choice in pick:
            pass
        else:
            pick.append(random_choice)
            if header in headers:
                pass
            else:
                headers.append(header)

    # formatting the output string
    # this accounts for the same pick twice and options from same/different columns

    first = pick[0]

    if (len(pick)) == 1:
        result = f'{first} only'
    else:
        if (len(headers)) == 1:
            second = pick[1].split(' ')[1]
        else:
            second = pick[1]
        result = f'{first} and {second}'

    return result
