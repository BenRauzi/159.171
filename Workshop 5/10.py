#input must be inside function according to question
def get_names():
    names = input("Enter names separated by a semi-colon: ").split(";")

    return [name.strip() for name in names] #list comprehension strips each item in list

print(get_names())