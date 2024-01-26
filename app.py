from env import sheet_list
from colour_roll import roller

commands = '''Hello, welcome! 
    sheet name = Rolls from that sheet.
    quit = Quits the program.
    (Type 'help' to repeat this message)
''' + f'    Active Sheets: {sheet_list}'

print(commands)

r = ""

while True:
    command = input("Instruction: ").lower()
    if command == "help":
        print(commands)
    elif command in sheet_list:
        roller(command)
        r = command
    elif command == "r" and r != "":
        roller(r)
    elif command == "r" and r == "":
        print("Please select a sheet to start!")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand...")

# if command in sheet_list, then run roller with sheet = command
