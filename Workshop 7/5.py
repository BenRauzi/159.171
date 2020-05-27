def sortMatrixItems(matrix):
    for x in range(len(matrix)):
        for i in range(len(matrix[x])):
            idx = i

            for j in range(i+1, len(matrix[x])):
                if matrix[x][idx] > matrix[x][j]:
                    idx = j

            matrix[x][i], matrix[x][idx] = matrix[x][idx], matrix[x][i]

    return matrix

def sortMatrix(matrix): #iterative selection sort that sorts the matrix assuming elements of each row are consecutive integers
    for i in range(len(matrix)):
        idx = i

        for j in range(i+1, len(matrix)):
            if matrix[idx][0] > matrix[j][0]:
                idx = j

        matrix[i], matrix[idx] = matrix[idx], matrix[i]

    return sortMatrixItems(matrix) 
    