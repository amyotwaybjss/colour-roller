from env import (wb, sheet_list, status, shuffle_options, category_list,
                 new_line, introduction, instructions, shuffle_detail)
from user_settings import sheet_category
from mode_select import active
from colour_roll import roller

# Setting initial values

r = ""
mode = "default"
shuffle = "mix"
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
        # else not needed as it will stay with initial/prior set setting

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
            print(roller(wb, command, shuffle))
            r = command

        elif command == "r":
            if r != "":
                print(roller(wb, r, shuffle))
            else:
                print("Please enter a valid sheet name to start!")

        elif command == "config":
            print(shuffle_detail)
            shuffle_set = input("Select: ".lower())
            if shuffle_set in shuffle_options:
                shuffle = shuffle_set

        elif command == "quit":
            break
            # this exits the while loop

        else:
            print("Sorry, I don't understand...")

print("See you next time!")
