#Assumptions:
#Question does not refer to spaces, or whitespace anywhere in the question - so we should assume that this also needs to be added to the list
#Or we should assume that it will not be tested for.

def letters(sentence):
    letter_totals = {} #create a blank dictionary to add letters to
    for letter in sentence:
        if letter in letter_totals: #if letter exists in dictionary increment value
            letter_totals[letter] += 1
        else: #if letter does not exist in dictionary add it and add one to the value
            letter_totals[letter] = 1
    return letter_totals