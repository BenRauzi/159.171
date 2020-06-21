minces, rafts = map(int, input().split())

mince_counts = [int(x) for x in input().split()]

for i in range(rafts):
    items = [int(x) for x in input().split()]
    lowest = -1

    i = 1
    while i < len(items) - 1:
        count = mince_counts[items[i] - 1]

        if count >= items[i + 1]:

            number = count // items[i + 1]

            if number < lowest or lowest == -1:
                lowest = number
        i += 2
    
    if lowest == -1:
        lowest = 0
        
    i = 1
    while i < len(items) - 1:
    
        mince_counts[items[i] - 1] -= (items[i + 1] * lowest)
        i += 2
    
    mince_counts.append(lowest)

print(mince_counts[-1])

