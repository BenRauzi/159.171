i = 0
while i < 6: #prints 0 through 5 except 3
    if i != 3:
        print("number {}".format(i)) #.format() creates more readable code (because python is not a strongly typed language i could be anything)
    else:
        print("*")
    i += 1