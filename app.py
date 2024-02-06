from env import sheet_list
from colour_roll import roller

r = ""
demo = False

instructions = f'''
    Hello, welcome! 
    sheet name = Rolls from that sheet.
    r = Re-Rolls using current settings.
    config = Adjusts randomness settings.
    demo = Turns demo mode on or off. 
    quit = Quits the program.
    (Type 'help' to repeat this message)
    
    Active Sheets: {sheet_list}'
    Demo Mode: {demo}
'''

print(instructions)

while True:
    command = input("Instruction: ").lower()
    if command == "help":
        print(instructions)
    elif command == "demo":
        demo = not demo
        print(f'Demo mode: {demo}')
    elif command in sheet_list:
        roller(command)
        r = command
    elif command == "r":  # nested if to avoid repeating code
        if r != "":
            roller(r)
        else:
            print("Please enter a valid sheet name to start!")
    elif command == "config":
        print("Whoops, I've not coded that one yet...")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand...")

# config settings:
# pick random mode - choices(match,mix,random)
# pick random priority - pick list first then col or pick col first then list
# how does this behaviour work in mix mode?
# demo mode hides/locks down certain options/maybe at the start a demo mode True/False can be set
