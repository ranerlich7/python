# my_number = int(input("Please enter a number "))
# if my_number > 0:
#     print("bigger than 0")

# my_number_1 = int(input("Please enter first number "))
# my_number_2 = int(input("Please enter second number "))
# my_action = int(input("Please enter action: 1 for add 2 for sub "))

# if my_action == 1:
#     print("adding result is", my_number_1 + my_number_2)
# elif my_action == 2:
#     print("sub result is", my_number_1 - my_number_2)
# else:
#     print("error please enter 1 or 2 as the action")

first_name = input("Please enter first name ")
last_name = input("Please enter last name ")
gender = input("Please enter gender:m for male, f for female ")

if gender == "m":
    print(f"Hello Mr {first_name} {last_name}")
else:
    print(f"Hello Mrs {first_name} {last_name}")
