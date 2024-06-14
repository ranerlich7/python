def zugi(my_arr):
    return_arr = []
    for item in my_arr:
        if item % 2 == 0:
            return_arr.append(item)
    return return_arr


print(zugi([1, 2, 3, 4]))
["a","baa","c","zzz"]