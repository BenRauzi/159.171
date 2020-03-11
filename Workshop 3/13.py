words = []

while True:
    word = input("Enter a word: ")
    if word.lower() == "end": #.lower() allows any casing from the input, prevents errors in real world scenarios
        break
    words.append(word)

print("The resulting list is " + str(words))