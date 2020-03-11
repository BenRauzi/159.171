name = input("Enter a name: ") #sets name to guess

print("*Start of game*")

while True:
    guess = input("Guess my name? ") #name user guesses

    if guess == name: #if guess is right, exit loop
        print("Got it!")
        break #exits loop

    print("Guess again") #if loop is not exited, guess again

   
print("*End of game*")