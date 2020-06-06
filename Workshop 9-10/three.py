"""
Generates a list of items on a menu from a .csv file and sorts items by calorie count in ascending order.
Only will include items between 100 and 200 calories.
.csv directory must be specified by assigning a directory to module variable 'filep'
"""

def menu_list():
    """
    Generates a menu from a .csv file of items between 100-200 calories (exclusive)
    Sorts the menu by order of calorie count (ascending)
    Module Variable 'filep' must be assigned before runtime. This must be the directory of the .csv menu file.
    """
    global menulist #allows menulist variable to exist in global module scope

    try:
        food_file = open(filep, "r")
    except NameError: #handles error and exits the function if filep not defined
        print("Module variable 'filep' not declared - you must specify a file directory")
        return 
    except FileNotFoundError: #handles error and exits function if file directory is invalid
        print(f"Invalid Directory - {filep} - You must specify a valid file directory")
        return

    menu = []
    for i in food_file.readlines()[1:]: #loops over the lines (excluding the heading line), breaking them into nested lists (question specified lists not classes)
        item = i.split(",")

        calories = int(item[2])
        if calories > 100 and calories < 200:
            menu.append([item[0], float(item[1]), int(item[2])])

    menulist = sorted(menu, key=lambda x: x[2]) #sorts by x[2] - the third item in the list - calories - using classes/objects would make this more readable

def show_menu():
    """
        Prints the menu generated in menu_list() in table format
        menu_list() must be called first
    """
    

    try:
        menulist
    except NameError: #handles error and exits the function if menulist is not defined
        print("Module variable 'menulist' undefined - You must generate a menu with menu_list() first")
        return 

    print(f"{'':<4}{'Food':<20}{'Calories':<15}{'Carbs':<15}") 

    for i, item in enumerate(menulist):
        print(f"{i+1:<4}{item[0]:<20}{item[2]:<15}{item[1]:<15}") #calories and carbs are opposite away round to the .csv
