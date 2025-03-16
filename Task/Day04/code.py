import random

correct_number = random.randint(1, 100)
attempts = 7  

print("🎯 Welcome to the Number Guessing Game!")
print(f"You have {attempts} attempts to guess the correct number.")

for i in range(attempts):
    try:
        guess = int(input(f"Attempt {i+1}/{attempts} - Guess the number (1-100): "))

        if guess < 1 or guess > 100:
            print("🚨 Please enter a number between 1 and 100.")
            continue

        if guess < correct_number:
            print("📉 Too low! Try again.")
        elif guess > correct_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the correct number {correct_number} in {i+1} attempts.")
            break
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")

else:
    print(f"❌ Sorry! You've used all {attempts} attempts. The correct number was {correct_number}. Better luck next time! 🚀")
