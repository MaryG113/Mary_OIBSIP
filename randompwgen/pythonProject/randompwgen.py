import string
import random

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
  """
  Generates a random password based on user-defined criteria.

  Args:
    length: The desired length of the password.
    include_uppercase: Whether to include uppercase letters (True by default).
    include_lowercase: Whether to include lowercase letters (True by default).
    include_numbers: Whether to include numbers (True by default).
    include_symbols: Whether to include symbols (True by default).

  Returns:
    A randomly generated password string.
  """

  # Define character sets based on user preferences
  characters = ""
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  # Generate and return the password
  password = "".join(random.sample(characters, length))
  return password

# Get user input for password length and character preferences
while True:
  try:
    password_length = int(input("Enter desired password length: "))
    if password_length < 1:
      raise ValueError("Password length must be at least 1.")
    break
  except ValueError:
    print("Invalid input. Please enter a positive integer.")

include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Generate and print the password
password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_symbols)
print(f"Generated password: {password}")