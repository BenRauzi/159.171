box_count, minutes = map(int, input().split())

n_p_b =  [int(x) for x in input().split()]
n_p_b.sort()

def moveLower(lower, i):
    upper = n_p_b[i + 1]
    if lower > upper:
        n_p_b[i], n_p_b[i + 1] = upper, lower
        try:
            moveLower(lower, i + 2)
        except:
            pass
        

def moveUpper(upper, i):
    lower = n_p_b[i - 1]

    if lower > upper:
        n_p_b[i], n_p_b[i - 1] = lower, upper
        try:
            moveUpper(upper, i - 2)
        except:    
            pass

for i in range(minutes):
   
    n_p_b[-1] -= 1
    n_p_b[0] += 1

    n_p_b.sort()
print(n_p_b[-1] - n_p_b[0]) 