def main():
    # Call both parts of the program from the main function
    process_numbers()
    check_username_access()


def process_numbers():
    """Ask for 5 numbers and display the statistics."""
    numbers = []

    # Prompt the user to enter 5 numbers
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    # Output the required information
    print(f"The first number is {int(numbers[0])}")
    print(f"The last number is {int(numbers[-1])}")
    print(f"The smallest number is {int(min(numbers))}")
    print(f"The largest number is {int(max(numbers))}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")  # Keep the average as a decimal


def check_username_access():
    """Check if the entered username is in the list of authorized users."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']

    # Ask the user for their username
    entered_username = input("Enter your username: ")

    # Check if the entered username is in the list of authorized users
    if entered_username in usernames:
        print("Access granted")
    else:
        print("Access denied")


# Call the main function to run the entire program
main()


