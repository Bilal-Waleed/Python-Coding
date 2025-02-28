# Write a Python function that takes a number as input and returns "Even" if the number is even and "Odd" if the number is odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))   
print(check_even_odd(10))  
print(check_even_odd(15))  
