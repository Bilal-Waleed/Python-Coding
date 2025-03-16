from datetime import datetime

def calculate_age():
    today = datetime.today() 
    current_year = today.year  

    birthdate_input = input("Enter your birthdate (DD/MM/YYYY): ").strip()

    try:
        birthdate = datetime.strptime(birthdate_input, "%d/%m/%Y")
        birth_year = birthdate.year

        if birth_year > current_year:
            print("❌ Error: Birth year cannot be in the future!")
            return

        age = current_year - birth_year

        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age -= 1  # Adjust age if birthday hasn't occurred this year

        print(f"\n🎉 You are {age} years old.")

        years_left = 100 - age
        if years_left > 0:
            print(f"⌛ You have {years_left} years left until you turn 100!")
        else:
            print("🎊 Congratulations! You are already 100 or older!")

    except ValueError:
        print("❌ Invalid date format! Please enter in DD/MM/YYYY format.")

calculate_age()
