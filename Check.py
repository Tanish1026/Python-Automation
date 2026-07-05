import re

# Pattern for a basic 5-digit US Zip Code

zip_pattern = r"^\d{5}$" # ^ means start of string and $ means end of string

user_input1 = "90210"
user_input2 = "90210\nearly"

if re.fullmatch(zip_pattern, user_input1):
    print("Valid Zip!")  # This will print
else:
    print("Invalid Zip!")

if re.fullmatch(zip_pattern, user_input2):
    print("Valid Zip!")
else:
    print("Invalid Zip!")  # This will print (contains letters)