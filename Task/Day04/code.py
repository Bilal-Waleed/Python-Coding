# Write a Python function that takes a number as input and returns "Even" if the number is even and "Odd" if the number is odd.

while True:
    try:
        num = input("\n🔢 Enter a number (or type 'exit' to quit): ")

        if num.lower() == 'exit':
            print("🚀 Exiting... Thanks for using the Even/Odd Checker!")
            break

        num = int(num)

        if num % 2 == 0:
            print(f"✅ {num} is an Even number.")
        else:
            print(f"🔢 {num} is an Odd number.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
