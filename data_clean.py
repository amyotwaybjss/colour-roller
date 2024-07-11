import re  # processes regex


def cell_clean(sheet, cell_row, cell_col):
    # this takes the cell specified and removes special characters, double spaces, and replaces whitespace with '_'
    input_cell = str(sheet.cell(cell_row, cell_col).value)
    special_char = re.sub(r'[^A-Za-z0-9\s]+', '', input_cell)
    # the r'' tells Python it is a raw string, so the \s does not error
    double_space = ' '.join(special_char.split())
    lower_clean = double_space.title().replace(' ', '_')
    # title() converts to camel case
    return lower_clean


def data_clean(workbook, name, dedup: bool):
    # loops through each sheet and column.
    # can either erase duplicates or keep them.
    for sheet in workbook:
        for column in range(1, sheet.max_column+1):
            col_values = []
            for row in range(1, sheet.min_row+1):
                # if first row, this is the header and is uppercase, added to 'header'
                header = (sheet.cell(row, column).value.upper())
                header_cell = sheet.cell(row, column)
                header_cell.value = header
            for row in range(2, sheet.max_row+1):
                # for other rows, skip empty cells and clean others
                cell = sheet.cell(row, column)
                if cell.value is None:
                    pass
                else:
                    cleaned = cell_clean(sheet, cell.row, cell.column)
                    cleaned_cell = sheet.cell(row, column)
                    if cleaned in col_values and dedup:
                        # removes duplicates if they exist in the column and the setting is on.
                        cleaned_cell.value = ''
                    else:
                        cleaned_cell.value = cleaned
                        col_values.append(cleaned)

    workbook.save(f'{name}_cleaned.xlsx')

