pizzas = {
    "Pizza 1": 5,
    "Pizza 2": 10,
    "Pizza 3": 15
}

order = ["Pizza 1", "Pizza 3"]

total = 0
for pizza in order:
    total += pizzas[pizza]

print(total)