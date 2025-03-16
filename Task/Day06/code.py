# Password Generator

import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("You must select at least one character type.")
        return None

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    try:
        length = int(input("Enter password length (min 8): "))
        if length < 8:
            print("Password must be at least 8 characters long.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        num_passwords = int(input("How many passwords to generate? "))

        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
            if password:
                print(password)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()