import random #put imports at the top of the page

class Game: #think of classes as objects... I.E physical objects that have have things done to them / can do things
    def __init__(self): #this function is called when the object is created
        self.total = 0 #assign a varible to the object

        while True:
            if self.total > 21:
                print("BUST!")
                break #exits the loop - game over
            else:
                print(self.total)
                ask_bool = input("Do you want to get another card? (y/n) ")
                if ask_bool.lower() != "y":
                    self.check_win() #calls a function that is a part of the object.
                    break #exits the loop - game over

                self.total += random.randint(0, 10)


    #Functions in object must have 'self' as the first parameter. This lets the object know how to interact with itself
    def check_win(self):  #you can have functions inside classes. Call them with 'self.func_name()'.
        print("Your final score was {}".format(self.total))


Game() #creates the class - __init__ function will be called automatically.