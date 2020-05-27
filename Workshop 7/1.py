def sumOfProducts(list_1, list_2):
    sum = 0

    for x in list_1:
        for y in list_2:
            sum += x * y

    return sum