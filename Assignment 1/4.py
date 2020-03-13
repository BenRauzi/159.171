words = []

while True:
    word = input("Enter a word: ").lower()

    if word == "quit":
        break #exits the loop if word == quit
    if word in words: #elif not needed because loop won't reach here if previous condition true
        print("Already seen - not adding to the list")
        continue #restarts at the top of the loop - skipping area below it


    words.append(word) #if loop reaches here, add word to list

print("You entered: " + str(words))

total_length = 0 #length of all words in the list
for word in words:
    length = len(word) #saving this as a variable saves doing the operation twice.
    print("The length of '{}' is: {}".format(word, length))
    total_length += length

print("The total length of all strings is: {}".format(total_length))