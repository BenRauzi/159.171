sentence = "The places you will go"

#we were specifically aksed to use SLICING for this task, .pop() or .remove() be more efficient.
index = sentence.index("you")

print(sentence[:index] + sentence[index + 4:])