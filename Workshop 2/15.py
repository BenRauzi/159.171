animal = input("Enter 'cat' or 'dog': ").lower()
language = input("What language would you like to translate to? German / French / Spanish: ").title()

if animal == "cat": #why can't I use dictionaries for this ;(
    if language == "German":
        word = "katze"
    if language == "French":
        word = "chat"
    if language == "Spanish":
        word = "gato"
if animal == "dog":
    if language == "German":
        word = "hund"
    if language == "French":
        word = "chien"
    if language == "Spanish":
        word = "perro"

print("The translation of {} into {} is {}".format(animal, language, word))