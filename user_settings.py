# USER SETTINGS #

wb_name = 'colours2'  # This is the name of the workbook to use (without xlsx)
force_refresh = False  # If True, will always replace cleaned xlsx

sheet_category = {
    "pii": ["personal", "private", "nonexistent"],
    "sensitive": ["private", "business1", "business2", "business3"]
}

# this creates a dictionary for sheet category permissions, controlled in mode_select.py
# note that the brackets are essential, even if there is only one entry!

# END USER SETTINGS #
