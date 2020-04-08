word = input("Enter a word at least 4 letters long: ")

for i in range(len(word)):
    if i != 3: #checks if this is the 4th iteration
        print(word[i])
    else:
        print("*")