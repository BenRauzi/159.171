import math

def equation(a, b): #two integer inputs
    x = (b + math.sqrt(b**2 - 1)) / (2*a)
    return x #does not specify to return to any specific rounding

def total():
    total = 0
    while True:
        a = input("Enter a: ")
        b = input("Enter b: ")

        if a == '' and b == '':
            break

        total += equation(int(a), int(b)) #question does not ask for error handling. We can assume a valid integer is always entered

    print(f"The total is {total}")

total()