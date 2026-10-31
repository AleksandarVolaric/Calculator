def calculate(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        if y == 0:
            raise ZeroDivisionError("Division with 0 is not possible")
        return x / y
    else:
        raise ValueError("Input the correct operation")


def main():
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    operation = input("Enter operation (+, -, *, /): ")

    try:
        result = calculate(x, y, operation)
    except ZeroDivisionError:
        print("Division with 0 is not possible")
        return
    except ValueError:
        print("Input the correct operation")
        return

    print("Your result is:", result)


if __name__ == "__main__": 
    main()