def main():
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        if y == 0:
            print("Division with 0 is not possible")
            return
        result = x / y
    else: 
        print("Input the correct operation")
        return


    print("Your result is:", result)





main()