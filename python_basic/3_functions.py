# def print_name(first_name, last_name):
#     print("my name is", first_name, last_name)

# print_name("Ran", "Erlich")
# print_name("Tal","bbbb")
# print_name("Pyoter","B")

# def get_full_name(first_name, last_name):
#     return first_name + last_name

# full_name = get_full_name("Ran", "Erlich")
# print(full_name)

#########################################################
# def is_positive(my_number):
#     return my_number > 0


# my_number = int(input("Please enter a number "))
# if is_positive(my_number):
#     print("bigger than 0")
#########################################################

# def double_my_numer(my_number):
#     my_number = my_number * 2
#     return my_number


# my_number = int(input("Please enter a number "))
# result = double_my_numer(my_number)
# print(result)

first_name = input("Please enter first name ")
last_name = input("Please enter last name ")
gender = input("Please enter gender:m for male, f for female ")


def first_last_name(f_name, l_name, my_gender):
    print("!!!!!",my_gender)
    if my_gender == "m":
        print(f"Hello Mr {f_name} {l_name}")
    else:
        print(f"Hello Mrs {f_name} {l_name}")

first_last_name("Raz","Mazliah","m")
first_last_name("Hodaya","Manzur","f")
first_last_name(first_name, last_name, gender)

def add(x,y):
    print("ADD")
    return x+y