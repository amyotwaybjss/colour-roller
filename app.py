from env import sheet_list

commands = '''
    Hello, this is a test!
    quit = Quits the program
    (Type 'help' to repeat this message)
''' + f'    Current Load: {sheet_list}'

print(commands)

while True:
    command = input("> ").lower()
    if command == "help":
        print(commands)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand...")

