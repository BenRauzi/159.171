def quicksort(xs):
    """Given indexable and slicable iterable, return a sorted list"""
    if xs: # if given list (or tuple) with one ordered item or more: 
        pivot = xs[0]
        # below will be less than:
        below = [i for i in xs[1:] if i < pivot] 
        # above will be greater than or equal to:
        above = [i for i in xs[1:] if i >= pivot]
        return quicksort(below) + [pivot] + quicksort(above)
    else: 
        return xs # empty list

print(quicksort([1,2,33,12,4123,12,3,23,16,1,43,123]))