"""
CP1404/CP5632 - Practical
CHeck password validity
"""
MIN_LENGTH=8

def main():
    #gets password and prints as stars
    password = get_password()
    while not is_valid_password(password):
        print("Invalid password")
        password = get_password()

    print_password_asterisks(password)

#print the password as asterisks
def print_password_asterisks(password):
    print(f"your password is {'*' * len(password)}")

#get a password and return it
def get_password():
    password = input("Enter your password: ")
    return password

#check the validity of the password
def is_valid_password(password):
    if len(password) < MIN_LENGTH:
        return False
    return True
main()
