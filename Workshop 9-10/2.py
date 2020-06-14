def menu_list(filep):   
    food_file = open(filep, "r")

    menu = []
    for i in food_file.readlines()[1:]:
        item = i.split(",")

        calories = int(item[2])
        if calories > 100 and calories < 200:
            menu.append([item[0], float(item[1]), int(item[2])])

    return sorted(menu, key=lambda x: x[2])

def show_menu(menu_list):
    print(f"{'':<4}{'Food':<20}{'Calories':<15}{'Carbs':<15}")

    for i, item in enumerate(menu_list):
        print(f"{i+1:<4}{item[0]:<20}{item[2]:<15}{item[1]:<15}") #calories and carbs are opposite away round to the .csv

def make_order():

    print("*** Order foods from the following menu ***")

    menu = menu_list("food.csv")
    show_menu(menu)

    ordered_items = []
    while True:
        command = input("Input food number: (q or Q to quit) ")

        if command.lower() == 'q':
            break

        try:
            pass
            
            item_number = int(command)

            if item_number > len(menu) or item_number <= 0:
                print("Please select a food that is in the menu list.")
                continue
            
            if menu[item_number - 1] in ordered_items:
                print("It is already selected. Please select others.")
                continue

            ordered_items.append(menu[item_number - 1])
        except ValueError:
            print("Please input the food number.")

    print("Here is your order:")

    show_menu(ordered_items)

make_order()