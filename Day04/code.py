def smart_calculator():
    while True:
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye! 👋")
            break

        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice! Please enter a valid option (1-4).")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            continue

        print("\n🧮 Calculating...")

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {round(result, 2)}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {round(result, 2)}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {round(result, 2)}")
        elif choice == '4':
            if num2 == 0:
                print("❌ Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {round(result, 2)}")

smart_calculator()
