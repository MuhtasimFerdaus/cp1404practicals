import string

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHAR_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in SPECIAL_CHARACTERS for char in password)

    if SPECIAL_CHAR_REQUIRED:
        return has_lower and has_upper and has_digit and has_special
    return has_lower and has_upper and has_digit

password = input("Enter password: ")
while not is_valid_password(password):
    print("Invalid password! Try again.")
    password = input("Enter password: ")

print(f"Your {len(password)}-character password is valid: {password}")