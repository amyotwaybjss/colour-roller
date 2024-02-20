from env import wb, wb_name
import re  # processes regex

# goal is to go through each sheet and apply the following:
# trim the values - done
# replace spaces with underscores - done
# remove special characters - done
# lowercase - done
# clear duplicates (set?)
# in env, need to check that clean ver exists, if not, run data_clean

sheet = wb['watercolours']
# cell = sheet.cell(4, 1)
#
# strip_ws = cell.value.strip()
# special_char = re.sub(r'[^A-Za-z0-9\s]+', '', strip_ws)
# double_space = re.sub(r' {2,}' , ' ', special_char)
# lower_clean = double_space.lower().replace(' ', '_')
#
# test = lower_clean
#
# print(test)


def cell_clean(cell_row, cell_col):
    input_cell = str(sheet.cell(cell_row, cell_col).value)

    special_char = re.sub(r'[^A-Za-z0-9\s]+', '', input_cell)
    double_space = ' '.join(special_char.split())
    lower_clean = double_space.lower().replace(' ', '_')

    return lower_clean


# print(cell_clean(4, 1))  # testing

# test = '+'.join(' words    morewords   wordywords wordswords    '.split())

# print(test)


# for sheet in wb:
#     cell = sheet.cell(1, 1)
#     print(cell.value)

for sheet in wb:
    for column in range(1, sheet.max_column+1):
        for row in range(1, sheet.min_row+1):
            header = (sheet.cell(row, column).value.upper())
            # print(header)
            header_cell = sheet.cell(row, column)
            header_cell.value = header
        for row in range(2, sheet.max_row+1):
            cell = sheet.cell(row, column)
            if cell.value is None:
                pass
            else:
                cleaned = cell_clean(cell.row, cell.column)
                # print(cleaned)
                cleaned_cell = sheet.cell(row, column)
                cleaned_cell.value = cleaned

wb.save(f'{wb_name}_cleaned.xlsx')


