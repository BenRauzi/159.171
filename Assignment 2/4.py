def makeTable(currencies):
    matrix = []

    for i in range(10, 101, 10):
        conversion = [i]
        for currency in currencies:
            conversion.append(i * currency[1])
        matrix.append(conversion)

    return matrix