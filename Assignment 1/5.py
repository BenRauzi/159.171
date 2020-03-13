lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()'

sentence = input("Enter a sentence: ")

char_counts = [0,0,0] #count of lower/upper/symbols

count = 0
for char_type in [lower, upper, symbols]: #loops through all 3 types in one nested for loops - done this way to minimise code reusing, even if not quite as fast.
    for char in sentence:
        if char in char_type:
            char_counts[count] += 1
    count += 1
    
print("There are {} lowercase letters.".format(char_counts[0]))
print("There are {} uppercase letters.".format(char_counts[1]))
print("There are {} symbols.".format(char_counts[2]))