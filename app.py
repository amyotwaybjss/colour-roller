from env import sheet_list, new_line, status
from colour_roll import roller
import inspect

# Setting initial values

r = ""
demo = "Demo Off"
step = 0

# Loop begins here

while True:

    # inspect.cleandoc is cleaning up the indentation
    instructions = new_line+inspect.cleandoc('''
            sheet name = Rolls from that sheet.
            r = Re-Rolls using current settings.
            config = Adjusts randomness settings.
            demo = Turns demo mode on or off.
            quit = Quits the program.
            (Type 'help' to repeat this message)
            ''')+(new_line*2)+status(demo, sheet_list)+new_line

    if step == 0:

        # first run of the loop only

        print("Hello, Welcome!")
        print(instructions)
        step = 1

    else:

        # user enters instruction

        command = input("Instruction: ").lower()

        # main body of the loop

        if command == "help":
            print(instructions)
        elif command == "demo":
            demo = "Demo On" if demo == "Demo Off" else "Demo Off"
            r = ""  # r needs to be reset here, in case it was previously set to a non-demo sheet
            print(status(demo, sheet_list))
        elif command in sheet_list:
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

print("See you next time!")

# NOTES #

# config settings:
# pick random mode - choices(match,mix,random)
# pick random priority - pick list first then col or pick col first then list
# how does this behaviour work in mix mode?
# demo mode hides/locks down certain options/maybe at the start a demo mode True/False can be set
