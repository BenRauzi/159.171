def make_list():
    my_list =[]
    for i in range(5): #more readable than 1,6
        my_list.append(i + 1)
    return my_list

print(make_list())