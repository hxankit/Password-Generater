"""
Project Requirements
Create a command-line password generator in Python that generates random passwords based on user-defined criteria, such as length and character types (letters, numbers, symbols). Allow users to specify password length and character set preferences.

"""
import random
import string

def generate_passwd(length, lowercase=True, uppercase=True, numbers=True, symbols=True):



  char_set = ""
  if lowercase:
    char_set += string.ascii_lowercase
  if uppercase:
    char_set += string.ascii_uppercase
  if numbers:
    char_set += string.digits
  if symbols:
    char_set += string.punctuation

  if not char_set:
    print("Oops! Please choose at least one character type.")
    return

  password = "".join(random.sample(char_set, length))
  return password


while True:
  try:
    length = int(input("How long should the password be (minimum 6 characters)? "))
    if length >= 6:
      break
    else:
      print("Password must be at least 8 characters long.")
  except ValueError:
    print("Please enter a number for password length.")

print("What kind of characters do you want to include? ")
lowercase = input("  - Lowercase letters (a-z)?(y/n) ").lower() == "y"
uppercase = input("  - Uppercase letters (A-Z)?(y/n) ").lower() == "y"
numbers = input("  - Numbers (0-9)?(y/n) ").lower() == "y"
symbols = input("  - Symbols (!@#$%^&*)?(y/n) ").lower() == "y"

passwd = generate_passwd(length, lowercase, uppercase, numbers, symbols)
print(f"Your randomly generated password: {passwd}")
