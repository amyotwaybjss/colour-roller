from user_settings import sheet_category
from env import category_list

# for values in sheet_category:
#     category_list.append(values)

category_list.extend(sheet_category)


def active(mode, cat, lis):

    mode = mode.lower()
    active_sheets = []
    categorised = []

    for category in cat.values():
        for sheet in category:
            if sheet not in categorised:
                categorised.append(sheet)
                # populates categorised with sheets that have a category in user_settings

    if mode == "admin":
        active_sheets = lis
        # admin user can see full list of sheets in doc

    elif mode in cat and mode != "default":
        for sheet in cat[mode]:
            if sheet in lis:
                active_sheets.append(sheet)
                # allows user to see sheets given to their category in the dictionary

    else:
        for sheet in lis:
            if sheet not in categorised:
                active_sheets.append(sheet)
                # default, allows user to see all uncategorised sheets

    return active_sheets


# let us assume the following:
# 1 'default' mode gives access to only unlabelled sheets
# 2 'x' mode gives access to 'x' only
# 3 'admin' mode gives access to all
