from art import logo


def add(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


calc = {"+": add,
        "-": subtraction,
        "*": multiplication,
        "/": division, }
def calculator():
    print(logo)
    number1 = float(input("What's the first number?:\n"))
    select_operator = input("+ \n- \n* \n/ \nPick an operation: \n")
    number2 = float(input("What's the next number?:\n"))

    if select_operator == "+":
        result = (calc["+"](number1, number2))
        print(f"{number1} + {number2} = {result}")
    elif select_operator == "-":
        result=(calc["-"](number1, number2))
        print(f"{number1} - {number2} = {result}")
    elif select_operator == "*":
        result=(calc["*"](number1, number2))
        print(f"{number1} * {number2} = {result}")
    elif select_operator == "/":
        result=(calc["/"](number1, number2))
        print(f"{number1} / {number2} = {result}")


    continue_calc = True
    while continue_calc:
        more_calc = input("Do you want to calculate more? write  y or n")
        if more_calc == "y":
            select_operator = input("+ \n- \n* \n/ \nPick an operation: \n")
            number3 = int(input("What's the next number?:\n"))
            if select_operator == "+":
                result2 = result
                result = (calc["+"](result, number3))
                print(f"{result2} + {number3} = {result}")
            elif select_operator == "-":
                result2 = result
                result =(calc["-"](result, number3))
                print(f"{result2} - {number3} = {result}")
            elif select_operator == "*":
                result2 = result
                result =(calc["*"](result, number3))
                print(f"{result2} * {number3} = {result}")
            elif select_operator == "/":
                result2 = result
                result=(calc["/"](result, number3))
                print(f"{result2} / {number3} = {result}")
        else:
            continue_calc = False
            print("\n"*50)
            calculator()
calculator()