#Ben Rauzi -- 20018179

import random as r #use alias r for random (for code readability by reducing clutter)


measure = ['tbsp', 'tsp', 'cup', 'mls']
ingredients = ['flour', 'baking powder', 'butter', 'milk', 'eggs', 'vanilla', 'sugar'] #named changed to reflect contents

main_ingredient = r.choice(['chocolate', 'banana', 'salted caramel', 'carrot', 'bran'])
baking_type = r.choice(['cake', 'brownie', 'cupcake', 'muffin']) #named changed to reflect contents

print("*** {} {} Recipe ***".format(main_ingredient, baking_type).title()) #Name of recipe
print("Ingredients: ")

print("{} {} {}".format(r.randint(1,3), r.choice(measure), main_ingredient)) #Prints amount, measure and type of main ingredient

final_ingredients = []
for i in range(5): #chooses 5 random ingredients from the list and prints amount, measure and type
    ingredient = r.choice(ingredients)
    final_ingredients.append(ingredient) #adds ingredient to the list

    print("{} {} {}".format(r.randint(1,3), r.choice(measure), ingredient))

print("Method:")

print("Mix the {}, {}, {}, {} and {} together.".format(final_ingredients[0],final_ingredients[1],final_ingredients[2],final_ingredients[3],final_ingredients[4])) #prints all ingredients in the list
print("Gently fold in the {}. ".format(main_ingredient))
print("Place mixture in {} tin and bake at {} degrees Celsius for {} minutes. ".format(baking_type, r.randint(170,220), r.randint(10,60))) #tin type, temp (170-222 incl.), time (10-60 incl.)
