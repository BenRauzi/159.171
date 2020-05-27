def sumOfValues(matrix):
    sum = 0
    for x in matrix:
        for y in x:
            sum += y
    
    print(sum)

m = [[5, 4], [2, 3], [6, 7]]
sumOfValues(m)