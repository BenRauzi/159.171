#these variable names are really ambiguous
def delete(x, my_list):
    my_list.remove(x)

    return my_list.count(x)


print(delete(3, [12, 22, 3, 46, 3, 77, 3]))
