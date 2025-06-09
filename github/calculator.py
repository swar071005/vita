def operator(operation, a, b):
    if operation == "addition":
        return a + b
    elif operation == "subtraction":
        return a - b
    elif operation == "multiplication":
        return a * b
    elif operation == "division":
        if b == 0:
            print("Error: Division by zero.")
            return None
        return a / b
    elif operation == "modulus":
        if b == 0:
            print("Error: Modulus by zero.")
            return None
        return a % b
    elif operation == "exponent":
        return a ** b
    else:
        print("Unknown operation.")
        return None

def main():
    print("Welcome to the calculator.")
    print("Choose an operator:")
    print("1. addition\n2. subtraction\n3. multiplication\n4. division\n5. modulus\n6. exponent")
    try:
        user_choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input.")
        return
    if user_choice == 1:
        operation_name = "addition"
    elif user_choice == 2:
        operation_name = "subtraction"
    elif user_choice == 3:
        operation_name = "multiplication"
    elif user_choice == 4:
        operation_name = "division"
    elif user_choice == 5:
        operation_name = "modulus"
    elif user_choice == 6:
        operation_name = "exponent"
    else:
        print("Invalid choice")
        return

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.")
        return

    result = operator(operation_name, a, b)
    if result is not None:
        print(f"The result of {operation_name} is: {result}")
    else:
        print("Error occurred.")
    print("Thank you for using calculator application.")


if __name__ == "__main__":
    main()