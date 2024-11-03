"""
CP1404/CP5632 - Practical
Determine score status using menu
"""
# Define the menu
MENU = """Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Main function to handle menu options."""
    score = get_valid_score()  # Get a valid score before entering the menu loop

    while True:
        print(MENU)  # Display the menu
        choice = input("Choose your option: ").upper()  # Make input case insensitive

        if choice == "G":
            score = get_valid_score()  # Get a valid score again
        elif choice == "P":
            result = evaluate_score(score, "User")  # Evaluate the score
            print(result)  # Print the result
        elif choice == "S":
            show_stars(score)  # Show stars based on the score
        elif choice == "Q":
            print("Thank you for using the program. Farewell!")  # Farewell message
            break
        else:
            print("Invalid option. Please choose again.")

def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def evaluate_score(score, name):
    """Evaluate the score and return the result as a string."""
    if score >= 90:
        return f"{name}: Excellent"
    elif score >= 50:
        return f"{name}: Passable"
    else:
        return f"{name}: Bad"

def show_stars(score):
    """Print stars based on the score."""
    star_count = int(score)  # Convert score to an integer for star printing
    print("Result: " + "*" * star_count)

# Execute the main function
main()
