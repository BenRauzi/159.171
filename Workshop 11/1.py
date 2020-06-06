class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste
    def __str__(self):
        return f"{self.taste} {self.name}"
    def orderFood(self, number):
        print(f"{number} times {self.taste} {self.name}")

class NZFood(Food):
    origin = "New Zealand"
    def changeOrigin(self, new_origin):
        NZFood.origin = new_origin

def createFood(food_list):
    return [Food(i[0], i[1]) for i in food_list]


class Test:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

new_test = Test("Ben")

print(new_test)