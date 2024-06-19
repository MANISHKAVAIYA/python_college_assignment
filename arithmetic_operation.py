# five code
def calculator():
    while True:
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))

        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = num1 / num2
        else:
            print("Invalid choice!")
            continue

        print(f"Result: {result:.2f}")

        repeat = input("Do you want to perform another operation? (y/n): ")
        if repeat.lower() != 'y':
            break

calculator()
