def ten():
    word = input("Enter a word: ")
    number = int(input("Enter a number: "))
    
    return word, number

word, number = ten()

print(word * number)