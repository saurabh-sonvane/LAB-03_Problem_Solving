# a calculator that takes two numbers and an operator from the user

num1 =int(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = int(input("Enter second number: "))

match operator:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")

    case "//":
        if num2 != 0:
            print("Result:", num1 // num2)
        else:
            print("Cannot divide by zero")

    case "%":
        if num2 != 0:
            print("Result:", num1 % num2)
        else:
            print("Cannot divide by zero")

    case "**":
        print("Result:", num1 ** num2)

    case _:
        print("Invalid operator")