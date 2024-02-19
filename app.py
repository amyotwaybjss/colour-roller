from env import (sheet_list, new_line, status)
from mode_select import category_list, active
from colour_roll import roller
import inspect

# Setting initial values

r = ""
mode = "Default"
step = 0
active_sheets = sheet_list

# Loop begins here

while True:

    # inspect.cleandoc is cleaning up the indentation
    # as instructions were not dynamically updating the status func was moved out
    instructions = new_line+inspect.cleandoc('''
            sheet name = Rolls from that sheet.
            r = Re-Rolls using current settings.
            config = Adjusts randomness settings.
            mode = Returns to the mode select screen.
            quit = Quits the program.
            (Type 'help' to repeat this message)
            ''')+(new_line*2)  # +status(mode, sheet_list)+new_line

    if step == 0:

        # first run of the loop only

        introduction = inspect.cleandoc('''
        Hello, Welcome! 
        Select a mode or press enter to skip.
        ''')

        print(introduction)

        init_mode = input("Mode: ").lower()

        if init_mode in category_list:
            mode = init_mode
        else:
            mode = "Default"

        active_sheets = active(mode)

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
        # elif command == "demo":
        #     mode = "Demo Mode" if mode != "Demo Mode" else "Default"
        #     r = ""  # r needs to be reset here, in case it was previously set to a non-demo sheet
        #     print(status(mode, sheet_list))
        elif command == "mode":
            step = 0
        elif command in active_sheets:
            print(roller(command))
            r = command
        elif command == "r":  # nested if to avoid repeating code
            if r != "":
                print(roller(r))
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

# NOTES #

# config settings:
# pick random mode - choices(match,mix,random)
# pick random priority - pick list first then col or pick col first then list
# how does this behaviour work in mix mode?
# demo mode hides/locks down certain options/maybe at the start a demo mode True/False can be set
