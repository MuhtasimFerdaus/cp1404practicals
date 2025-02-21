valid_input = False
while not valid_input:
    try:
        number = int(input("Enter an integer: "))
        valid_input = True  # Exit loop if input is valid
    except ValueError:
        print("Invalid input; please enter a valid integer.")

print(f"You entered {number}.")