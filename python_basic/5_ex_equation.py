""" 
1. get 3 variables
2. check that determinatta >=0
3. check that a!=0
4. solve
"""


def check_det(a, b, c):
    result = b * b - 4 * a * c
    return result >= 0


def check_den(a):
    return a != 0
    # if a == 0:
    #     return False
    # else:
    #     return True


a = int(input("please enter number a "))
b = int(input("please enter number b "))
c = int(input("please enter number c "))
test1 = check_det(a, b, c)
test2 = check_den(a)
print("first test 1 (det):", test1)
print("first test 2 (den):", test2)

if (test1 and test2):
    sol1 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
    sol2 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)
    print("the solutions are:", sol1, sol2)
else:
    print("test failed, not calculating")
