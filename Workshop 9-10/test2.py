def menu_list():

    filep=open('food.csv')
    lines=filep.readlines()
    filep.close()
    list1=[]
    ordlist=[]

    for line in lines:
        x=line.split(",")
        list1.append(x)

    list2=list1[1:]
    for num in list2:
        items = num[0]
        carbs = num[1]
        calories = num[2]


        if int(calories)>100 and int(calories)<200:

            food=items,carbs,calories
            ordlist.append(food)

            ordlist.sort(key=lambda calories: calories[2])
    
    return ordlist

            #need to work out how to sort list and get results in a nested list


def show_menu(menulist):#display the menu in coloumns

    print('Food', '\t', 'Calories', 'Carbs', sep='\t')

    for row in menulist:
        print(row)
        rows = (row[0],row[2],row[1])
        print("{:4}{:20}{:15}{:15}".format("", "Food","Calories","Carbs"))


def make_order():
    menulist = menu_list()
    show_menu(menulist)
    foodlist=[]
    x = 0
    while True:
        foodnumber = input("Input food number: (q or Q to quit) ")
        foodnumber.lower()
        if foodnumber == "q":
            print(foodlist)
            break
        if foodnumber not in foodlist:
            try:
                foodnumber=int(foodnumber)-1
                foodnumber=menulist[foodnumber]
                foodnumber=foodnumber[0]
            except:
                pass




make_order()