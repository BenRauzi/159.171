words = []

while True:
    word = input("Enter a word: ").lower()

    if word == "quit":
        break

    words.append(word)

print("You entered: " + str(words))
