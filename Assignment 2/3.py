text = []
    
def add_handler():
    while True:
        line = input("Add a line: ")

        if line.lower() == "#":
            break

        text.append(line)

#could call these recursively instead of looping - but looping works fine
def remove_handler():
    while True:
        try:
            line = int(input("Line number: "))
        except:
            continue

        if line > len(text) or line < 0:
            continue

        del text[line - 1]
        break

def replace_handler():
    while True:
        try:
            line = int(input("Replace line number: "))
        except:
            continue

        if line > len(text) or line < 0:
            continue

        line_text = input("Replacement string: ")

        text[line - 1] = line_text
        break

def replace_string_handler():
    find_string = input("Find string: ")
    replace_string = input("Replace with: ")

    for i in range(len(text)):
        if find_string in text[i]:
            text[i] = text[i].replace(find_string, replace_string)

def copy_handler():
     while True:
        try:
            start_line = int(input("Start line number: "))
            end_line = int(input("End line number: "))
        except:
            continue

        if (start_line > len(text) or start_line < 0) or (end_line > len(text) or end_line < 0):
            continue

        text.append(" ".join(text[start_line - 1: end_line]))
        break

while True:
    command = input("Command a, d, r, f, p, c, q: ").lower()

    if command == "q":
        break
    elif command == "a":
        add_handler()
    elif command == "d":
        remove_handler()
    elif command == "r":
        replace_handler()
    elif command == "f":
        replace_string_handler()
    elif command == "p": #copy/paste
        copy_handler()
    elif command == "c":
        text = []
    
    for i in range(len(text)):
        print(f"{i + 1}: {text[i]}")
        
    print("")