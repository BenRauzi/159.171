import turtle

wn = turtle.Screen() #creates a graphics window
alex = turtle.Turtle() #create a turtle named alex

alex.color("red")

for i in range(4): #make a 2x1 rectangle
	alex.forward(75 * ((i + 1)%2 + 1)) 
	alex.left(90)

wn.exitonclick() 