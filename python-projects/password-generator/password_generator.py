import random
import string

length = int(input("Enter password length: "))

if length < 8:
    print("Password length must be at least 8 characters.")
    exit()
    
include_numbers = input("Include numbers? (y/n): ").lower()
include_symbols = input("Include symbols? (y/n): ").lower()

characters = string.ascii_letters

if include_numbers == "y":
    characters += string.digits

if include_symbols == "y":
    characters += string.punctuation

count = int(input("How many passwords to generate? "))

if length < 10:
    strength = "Weak"
elif length < 15:
    strength = "Medium"
else:
    strength = "Strong"

for p in range(count):
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print(f"\nGenerated Password {p+1}: {password}")

print(f"\nPassword Strength: {strength}")
