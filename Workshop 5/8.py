words = input("Enter a sentence at least 3 words long: ").split()

if len(words) >= 3:
    print(words[:2])
else:
    print("You must enter a 3 word long sentence")
