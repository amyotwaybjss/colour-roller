import re  # processes regex


def cell_clean(sheet, cell_row, cell_col):
    input_cell = str(sheet.cell(cell_row, cell_col).value)
    special_char = re.sub(r'[^A-Za-z0-9\s]+', '', input_cell)
    # the r'' tells Python it is a raw string, so the \s does not error
    double_space = ' '.join(special_char.split())
    lower_clean = double_space.lower().replace(' ', '_')
    return lower_clean


def data_clean(workbook, name):
    for sheet in workbook:
        for column in range(1, sheet.max_column+1):
            for row in range(1, sheet.min_row+1):
                header = (sheet.cell(row, column).value.upper())
                header_cell = sheet.cell(row, column)
                header_cell.value = header
            for row in range(2, sheet.max_row+1):
                cell = sheet.cell(row, column)
                if cell.value is None:
                    pass
                else:
                    cleaned = cell_clean(sheet, cell.row, cell.column)
                    cleaned_cell = sheet.cell(row, column)
                    cleaned_cell.value = cleaned

    workbook.save(f'{name}_cleaned.xlsx')

# this does not yet clear duplicates
