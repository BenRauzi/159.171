###Zacks Totally Vegan Vegetables###

# imports#
import random
import time

# Constants#
MENU_SLEEP = 0.5  # wait time between printing the menu items.#
AFTER_MENU_SLEEP = 3.5  # made as a variable so they can be easily changed#

# Globals#
# lists#
menu = ["Carrot", "Potato", "Beetroot Sub", "Vege Pie", "Totally no B just LT", "Vegan Beef Steak", "A Single Bean", ]
prices = ["1", "2", "6", "12", "4", "21", "50"]
receipt = []  # blank list which will have their items added to#


### Functions ###
# function for user choosing what foods they would like #
# Witch are added to the 'receipt' list and prices witch are added to the 'bill'#
def order(bill=0):
    try:
        pick = int(input("What would you like to order? (Put in the Number) or type 10 to print the menu\n").strip()) - 1
        if pick == 9:
            for i in range(0, len(menu)):
                print("{}.{} costing ${}".format(i + 1, menu[i], prices[i]))
            order()
        elif pick >= 0 and pick < len(menu):  # makes sure the number they put in has a corresponding menu item #
            print(menu[pick])
            receipt.append(menu[pick])
            bill += int(prices[pick])
            while True:
                continue_shop = input("Would you like to order something else? (y/n)\n").lower().strip()
                if continue_shop == "y" or continue_shop == "yes":
                    order()
                    break
                elif continue_shop == "n" or continue_shop == "no":
                    print("Your order is {}".format(receipt))  # prints the list of foods they wanted #
                    print("Costing ${}".format(bill))  # prints the total cost of the food they wanted #
                    end()
                    break
                else:
                    print("y or n")
                    continue
        else:
            print("Pick a number that has a food item")
            order()
    except ValueError:  # if the input would cause an error it instead prints#
        print("Please put the number of one of our food items")  # a sentence and takes them back to the start#
        order()


# function for printing the menu form the list#
def full_menu():
    for i in range(0, len(menu)):
        print("{}.{} costing ${}".format(i + 1, menu[i], prices[
            i]))  # prints the item number on the list +1 so it starts at 1 rather than 0#
        time.sleep(MENU_SLEEP)  # wait time inbetween printing items#
    time.sleep(AFTER_MENU_SLEEP)
    main()


# function for the picking of a random item from the 'menu' list#
def pick_for_you():
    print("The chef recommends our amazing {}".format(random.choice(menu)))
    main()


# function for printing some information about the food
def info():
    print('We only use the highest quality NZ beef in all of our "vegetables"')
    main()


# function for user inputting a suggested food item which is saved to a file#
def new_item():
    print("Zacks Totally Vegan Vegetables is always looking to expand our menu\n"
          "so we are happy to take your suggestions")
    new = input("What is your food suggestion?")
    if 3 < len(new) <= 20:  # makes sure the input is smaller than 21 and greater than 3#
        file = open("suggestions.txt", "w")  # writes the input to a file to be read later#
        file.write(new)  # Writes item to the list, followed by a new line.
        file.close()
        print("Thank you. Your suggestion will be looked at.\n"
              "and next time you order you may see your item.")
        main()
    else:
        print("Please put in a suggestion that is at least 3 letters long and no longer than 20")
        new_item()


# function prints a goodbye and stops program#
def end():
    print("Thank you for shopping with Zacks Totally Vegan Vegetables. Please come again.")


# function is the menu which all the other functions come off.#
# Asks what they want to do and calls the required function#
def main():
    print("Welcome to Zacks Totally Vegan Vegetables the most trusted Vegan takeaway of all time")
    choice = input("Please Type\n"  # menu#
                   "a to order.\n"
                   "b to see the menu.\n"
                   "c to see the chefs pick for you.\n"
                   "d to get more info on our ingredients.\n"
                   "e to suggest a new food item\n").lower().strip()
    if choice == "a":
        order()
    elif choice == "b":
        full_menu()
    elif choice == "c":
        pick_for_you()
    elif choice == "d":
        info()
    elif choice == "e":
        new_item()
    else:  # if anything other than a-e is input will ask them to do it again#
        print("Please type a, b, c, d or e")
        main()


# calls the main function to start the program#
main()