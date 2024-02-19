from env import sheet_category, sheet_list

category_list = ["default", "admin"]

for values in sheet_category:
    category_list.append(values)

# test #
print(f'sheet_category: {sheet_category}')
print(f'category_list: {category_list}')
print(f'sheet_list: {sheet_list}')
print('')


def active(mode):

    mode = mode.lower()
    active_sheets = []
    categorised = []

    for category in sheet_category.values():
        for sheet in category:
            if sheet not in categorised:
                categorised.append(sheet)

    if mode == "admin":
        active_sheets = sheet_list

    elif mode in sheet_category and mode != "default":
        for sheet in sheet_category[mode]:
            if sheet in sheet_list:
                active_sheets.append(sheet)

    else:
        for sheet in sheet_list:
            if sheet not in categorised:
                active_sheets.append(sheet)

    return active_sheets


# let us assume the following:
# 1 'default' mode gives access to only unlabelled sheets
# 2 'pii' mode gives access to 'pii' only
# 3 'sensitive' mode gives access to 'sensitive' only
# 4 'admin' mode gives access to all
