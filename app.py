from env import (wb, sheet_list, new_line, status, instructions, settings_detail, introduction)
from user_settings import sheet_category
from mode_select import category_list, active
from colour_roll import roller

# Setting initial values

r = ""
mode = "Default"
setting = "mix"  # this needs to be changeable in the app
step = 0
active_sheets = sheet_list

# Loop begins here

while True:

    if step == 0:

        # first run of the loop only

        print(introduction)

        init_mode = input("Mode: ").lower()

        if init_mode in category_list:
            mode = init_mode
        else:
            mode = "default"

        active_sheets = active(mode, sheet_category, sheet_list)

        print(instructions)
        print(status(mode, active_sheets)+new_line)

        step = 1
        r = ""

    else:

        # user enters instruction

        command = input("Instruction: ").lower()

        # main body of the loop

        if command == "help":
            print(instructions)
            print(status(mode, active_sheets) + new_line)

        elif command == "mode":
            step = 0

        elif command in active_sheets:
            print(roller(wb, command, setting))
            r = command

        elif command == "r":  # nested if to avoid repeating code
            if r != "":
                print(roller(wb, r, setting))
            else:
                print("Please enter a valid sheet name to start!")

        elif command == "config":
            print("Whoops, I've not coded that one yet...")

        elif command == "quit":
            break  # this exits the while loop

        else:
            print("Sorry, I don't understand...")
            # this is a generic error, we want an error for access not allowed

print("See you next time!")
