"""
CP1404/CP5632 - Practical
A menu-driven program that greets the user based on their input.
Prompts the user for their name and offers options to say hello, goodbye, or quit.
"""
# Get name from the user
name = input("Enter name: ")

# Display the menu and get the initial choice
choice = input('(H)ello\n(G)oodbye\n(Q)uit\n>>> ').strip().upper()

# Loop until the user chooses to quit
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display the menu again and get the next choice
    choice = input('(H)ello\n(G)oodbye\n(Q)uit\n>>> ').strip().upper()

# Display finished message
print("Finished.")
