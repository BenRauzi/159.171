pizza_list = { "Oof Pizza": 5, "Phat Oof Pizza": 10,  "Papas Burger Pizza": 3, "Potato-top Pizza": 12, "Burnt piece of trash pizza": 1} #List of Pizzas on the menu
class Pizza:
    def __init__(self, name, number):
        self.name, self.number = name, number
class Order: #Order Class/Data Type
    new_orders = []
    def __init__(self, pizzas):
        self.pizzas = [Pizza(i[0], i[1]) for i in pizzas]
        self.new_orders.append(self)  
def add_order(): #add an order to the orders
    order_pizzas = []
    while True:
        pizza_name = input("Enter Pizza Name (or quit): ").title()
        if pizza_name == "Quit": #finished the order
            break
        if not(pizza_name in pizza_list.keys()): #Prevents people from ordering pizzas that are not on the menu
            print("Bad Pizza Name! - Pizza must be a valid pizza")
            continue
        try:
            quantity =  int(input("Enter Quantity: ")) #num of pizzas to order (int)
            if quantity <= 0:
                raise ValueError
        except ValueError: #retry if quantity is not a valid input (not an integer or < 0)
            print("Invalid Quantity - start again")
            continue
        order_pizzas.append([pizza_name, quantity])
    order = Order(order_pizzas) if len(order_pizzas) > 0 else 0
def main(): #main function loop that controls what functions are called when
    while True:
        cmd = input("Enter Command (add, list, prices, export, quit): ").lower()
        if cmd == "quit":  #ends program
            break
        elif cmd =="add": #add a new order
            add_order()
        elif cmd == "list": #print off a list of all current orders
            [print(f"Order: {Order.new_orders.index(x) + 1}" + "".join([f"\n   Pizza: {i.name}, Quantity: {i.number}" for i in x.pizzas])) for x in Order.new_orders]
        elif cmd == "prices": #print out the names and prices of available pizzas
            [print(f"Pizza Name: {y}, \n  Price: ${pizza_list[y]}") for y in pizza_list]
        elif cmd == "export": #save the orders to a file for the chef
            file = open("oof.ini", "w+")
            file.write("\n".join([(f"Order: {Order.new_orders.index(x) + 1}" + "".join([f"\n   Pizza: {i.name}, Quantity: {i.number}" for i in x.pizzas])) for x in Order.new_orders]))
            file.close()
main()