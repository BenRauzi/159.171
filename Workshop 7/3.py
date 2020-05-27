def incrementValues(matrix):

    size = len(matrix[0])
    for x in range(len(matrix)):
        for y in range(size):
            matrix[x][y] += 1
        

    return matrix