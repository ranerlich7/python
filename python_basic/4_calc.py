def plus(x, y):
    print(f"x + y =")
    return x + y


def minus(x, y):
    print(f"x - y =")
    return x - y


def calculate(number1, number2, action):
    result = ""
    if action == "+":
        result = plus(number1, number2)
    elif action == "-":
        result = minus(number1, number2)
    return result


number1 = int(input("please enter first number "))
number2 = int(input("please enter second number "))
action = input("please enter action + - * /")
final_result = calculate(number1, number2, action)
print("the result is:", final_result)
