import random

names = ["Bronco", "Beau", "Braxton", "Brody", "Blake", "Ben", "Bryce"]

dog_names = int(input("How many dogs would you like names for?: "))
random.shuffle(names)

print(names[0:dog_names])


names_db = open("oof.ini", "w+")

for name in names[0:dog_names]:
    names_db.write(name + "\n")

names_db.close()