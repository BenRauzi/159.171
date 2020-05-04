import random
import time

menu = ["Carrot", "Potato", "Beetroot Sub", "Vege Pie", "Totally no B just LT", "Vegan Beef Steak", "A Single Bean", ]

prices = ["1", "2", "6", "12", "4", "21", "50"]

receipt = []


bill = 0


def order(bill=0):
    pick = int(input("What would you like to order? (Put in the Number) or type 10 to print the menu\n"))
    pick -= 1
    if pick == 10:
        for i in range(0, len(menu)):
            print("{}.{} costing ${}".format(i + 1, menu[i], prices[i]))
            order()
    elif pick > 0:
        print(menu[pick])
        receipt.append(menu[pick])
        pick += 1
        bill += int(prices[pick])
        while True:
            contine = input("Would you like to order somthing else? (y/n)\n").lower().strip()
            if contine == "y":
                order()
                break
            elif contine == "n":
                print("Your order is {}".format(receipt))
                print("Costing ${}".format(bill))
                end()
                break
            else:
                print("y or n")
                contine
    else:
        print("Must be greater than 0")
        order()


def full_menu():
    for i in range(0, len(menu)):
        print("{}.{} costing ${}".format(i + 1, menu[i], prices[i]))
        time.sleep(.5)
    time.sleep(3)
    main()


def pick_of_day():
    print("Todays 'pick of the day' is our amazing {}".format(random.choice(menu)))
    main()


def info():
    print('We only use the highest quality NZ beef in all of our "vegetables"')


def new_item():
    print("Zacks Totally Vegan Vegetables is always looking to expand our menu\n"
          "so we are happy to take your suggestions")
    new = input("What is your food suggestion?")
    file = open("suggestions.txt", "w")
    file.write(new)  # Writes item to the list, followed by a new line.
    file.close()
    print("Thank you. Your suggestion will be looked at.\n"
          "and next time you order you may see your item.")
    main()


def end():
    print("Thank you for shopping with Zacks Totally Vegan Vegetables. Please come again.")


def main():
    print("Welcome to Zacks Totally Vegan Vegetables the most trusted Vegan takeaway of all time")
    choice = input("Please Type\n"
                   "a to order.\n"
                   "b to see the menu.\n"
                   "c to see the chefs pick of the day.\n"
                   "d to get more info on our ingredients.\n"
                   "e to suggest a new food item\n")
    if choice == "a":
        order()
    elif choice == "b":
        full_menu()
    elif choice == "c":
        pick_of_day()
    elif choice == "d":
        info()
    elif choice == "e":
        new_item()
    else:
        print("Please type a, b, c, d or e")
        main()


main()
