number = int(input("Enter a number: "))
total = 0

for i in range(1, number + 1):
    num_sqr = i**2
    print("The square of {} is {}".format(i, num_sqr))
    total += num_sqr

print("The sum of the squares is {}".format(total))