import random as ran


def roller(workbook, sheet, shuffle, priority):  # priority gets column/value
    # e.g. roller(wb, watercolours, match, column)

    sheet_name = workbook[sheet]
    max_col = sheet_name.max_column
    max_row = sheet_name.max_row
    all_columns = list(range(1, max_col + 1))

    if shuffle == "random":
        shuffle = ran.choice(["match", "mix"])

    matching = max_col == 1 or shuffle in ("match", "single")  # result binary TRUE/FALSE

    pick = []
    headers = []

    if priority == "column":

        # select a random column from chosen sheet

        col_select1 = ran.randint(1, max_col)
        col_select2 = col_select1

        # if more than one column, set col_select2 to be different column

        if not matching:
            while col_select2 == col_select1:
                col_select2 = ran.randint(1, max_col)

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

            if random_choice in pick or (len(pick) == 1 and shuffle == "single"):
                pass
            else:
                pick.append(random_choice)
                if header in headers:
                    pass
                else:
                    headers.append(header)

    else:

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
