def makeTable(currencies):
    matrix = []

    for i in range(10, 101, 10):
        conversion = [i]
        for currency in currencies:
            conversion.append(i * currency[1])
        matrix.append(conversion)

    return matrix

def printTable(currencies, table):
    
    print("$NZ", end=" \t")
    for currency in currencies:
        print(currency[0], end=" \t")
    print()

    for row in table:
        for cell in row:
            print("{:.2f}".format(cell), end=" \t")
        print()
