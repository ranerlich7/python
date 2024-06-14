# def zugi(my_arr):
#     return_arr = []
#     for item in my_arr:
#         if item % 2 == 0:
#             return_arr.append(item)
#     return return_arr


# print(zugi([1, 2, 3, 4]))
# ["a","baa","c","zzz"]


def biggest_in_array(input_arr):
    my_max = input_arr[0]
    for item in input_arr:
        try:
            if item > my_max:
                my_max = item
        except Exception as ex:  # ex = error
            print(ex)
            print("error in item", item)
    return my_max


# result = biggest_in_array([1,2,3,4])
# print(result)
# result = biggest_in_array(["aa","bb","cc"])
# print(result)
result = biggest_in_array(["aa", 10, "cc"])
print(result)
