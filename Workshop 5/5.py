word = input("Enter a word: ")

for i in range(1, len(word) + 1): #this method requires less calculations per iteration. Calculation (not loop) O(1) not O(n)
    print(word[-i])