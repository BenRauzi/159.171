item_price = float(input("Enter an amount: "))
item_name = input("Enter an item name: ")

for tax_amount in range(5, 30, 5): #range() must use integers. Therefore another step is required.
    print("{}% tax on a {} costing ${:.2f} is ${:.2f}".format(tax_amount, item_name, item_price, item_price * (tax_amount / 100))) #calculates tax cost
    