import random #Imports the random module

pizza_flavours = ["Meatlovers", "Vegetarian", "Pepperoni", "Hawaiian", "Triple cheese", "Cheese", "Vegan", "Italian"]
receipt = []#blank list to add the order to

def order(): #ordering function asks the user what they want to order
    try:
        pick = int(input("What would you like to order? (Put in the Number)\n"))
        if pick > 0 and pick < len(pizza_flavours):#only procceds if the number user chose is inbetween the values of the list
            pick -= 1
            receipt.append(pizza_flavours[pick])
            print(receipt)
        else: #if user picks negative or higher than 8 re runs the function
            print("Order has to be higher than 0 and lower than 8")
            order()
    except ValueError:#if user types a string or anything thats not a number re runs the function
        print("Must write a whole number")
        order()

def invoice():
    file = open("invoice.txt", "w+")#opens the order text document
    for pick in receipt:
        file.write(pick + "\n")#loops through the pizzas that the user picked in recepit then prints to document
        print("You've ordered a {} pizza ".format(pick))
    file.close()#closes the file

def invoice_free():#invoice for the free part of the order if you roll the right number
    file = open("invoice.txt", "w+")#same as above opens the invoice document
    file.write("You got your order for free, your order is: \n")
    for pick in receipt:
        file.write(pick + "\n")#same as above loops through pick in recepit except prints that your order is free as well.
        print("You've ordered a {} pizza ".format(pick))
    file.close()#closes the file

def roll():#roll function to see if you get your order for free or not
    while True:
        roll = input("Would you like to roll for a 1/10 chance for your order to be free?(yes/no)").lower().strip()
        if roll == "yes":
            y = random.randint(1, 10)#picks random number between 1 and 10
            print(y)
            if y == 2:#if the random number is 2 they get a free order
                print("Congrats your order is now free!")
                invoice_free()#calls the invoice_free function
            else:
                print("better luck next time")#if number isnt 2 prints better luck next tiem and runs normal invoice
                invoice()
            break
        elif roll == "no":#if user doesnt want to roll it runs invoice
            invoice()
            break
        else:
            print("must answer yes or no")#handles invalid inputs such as a number or anything other than yes or no

def print_list():#this function assigns each pizza flavour a number for the ordering system
    print("\nOur list of Pizza flavours.\n")
    for i in range(0, len(pizza_flavours)):#loops through all of the pizza flavours printing them on the screen with a number
        print("{}.{}".format(i+1, pizza_flavours[i],))

def menu():
    choice = input("\nDo you want to. \n1: Take your order? \n2: Print the full list of pizza flavours we have available?").strip()#asking the user what they want to do
    if choice == "1":#if its one they want to take their order so runs order
        order()
    elif choice == "2": #if its 2 they want to print the list so it runs the print_list function after this it runs main
        print_list()
        menu()
    else: #handles invalid inputs any number that inst 1 or 2 and anything else like spaces and stings
        print("\nMust put either 1 or 2")
        main()#runs main again

def main():#the main function```````````````````````````````
    menu()#runs menu
    print(3)
    while True:
        retry = input("Would you like to order another pizza? yes/no")#after the user has ordered a pizza it comes back to here and asks them if they want to order another
        if retry == "yes":#if the user answers yes it calls order
           order()
        elif retry == "no":#if the user answers no it runs roll
            roll()
            break
        else:#handles invalid inputs such as anything that isnt yes or no
            print("must answer yes or no")

main()#main function to run everything.