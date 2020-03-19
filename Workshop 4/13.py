def sentence():
    sentence = input("Enter a sentence: ")

    if 'b' in sentence.lower():
        return "The sentence contains b/B"
    else:
        return "The sentence does NOT contain b/B"
    
print(sentence())