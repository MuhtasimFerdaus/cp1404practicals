"""
CP1404/CP5632 - Practical
CHeck password validity
"""
MIN_LENGTH=8

def main():
    #gets password and prints as stars
    password=input("Enter your password: ")
    while not is_valid_password(password):
        print("Invalid password")
        password=input("Enter your password: ")

    print(f"your password is {'*' * len(password)}")
def is_valid_password(password):
    if len(password) < MIN_LENGTH:
        return False
    return True
main()
