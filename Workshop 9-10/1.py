class Food:
    def __init__(self, details):
        self.name = details[0]
        self.carbs = float(details[1])
        self.calories = int(details[2])

food_file = open("food.csv", "r")

food_list = [Food(i.split(',')) for i in food_file.readlines()[1:]] #reads file, splits it into sublists based on each line. Removes first line (heading line)

food_file.close()

lowest_calories = min(food_list, key=lambda x: x.calories)

print(f"Food with lowest calories: {lowest_calories.name}, {lowest_calories.calories} calories, {lowest_calories.carbs} carbs.")

no_carbs = sorted([i for i in food_list if i.carbs == 0 and i.name != None], key=lambda x: x.name)

for i in no_carbs:
    print(f"{i.name} {i.calories}")
