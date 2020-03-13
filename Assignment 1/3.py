words = []

while True:
    word = input("Enter a word: ").lower()

    if word == "quit":
        break
    if word in words: #elif not needed because loop won't reach here if previous condition true
        print("Already seen - not adding to the list")
        continue


    words.append(word) #if loop reaches here, add word to list

print("You entered: " + str(words))
