import math

radius = int(input("Enter the radius: "))

if radius > 0:
    volume = (4 * math.pi) / 3 * (radius ** 3)
    print("The volume of a sphere with a radius of {} is {:.2f}".format(radius, volume))
else:
    print("Invalid radius, must be a positive number")