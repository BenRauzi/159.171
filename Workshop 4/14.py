def profit(amount):
    return amount * 0.15

def total_profit(good_1, good_2, good_3):
    return profit(good_1) + profit(good_2) + profit(good_3)

x, y, z = 4.55, 150, 10.05
print("The total profit on ${:0.2f}, ${:0.2f}, and ${:0.2f} is ${:0.2f}".format(x, y, z, total_profit(x, y, z)))