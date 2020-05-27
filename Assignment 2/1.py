while True:
    command = input("Enter a command: ")

    if command == "quit":
        break

    if (command[:10].lower() == "simon says"):
        print(command[11:])