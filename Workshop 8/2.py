def reverse2nd(t):
    return tuple([t[x] for x in range(len(t), 0, -1) if x % 2 == 1])