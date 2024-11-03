"""
CP1404/CP5632 - Practical
Program to determine score status
"""
def main():
    # Get user score
    score = float(input("Enter score: "))
    result = evaluate_score(score, "User")  # Call function to evaluate the score
    print(result)  # Print the result

def evaluate_score(score, name):
    """Evaluate the score and return the result as a string."""
    if score >= 90:
        return f"{name}: Excellent"
    elif score >= 50:
        return f"{name}: Passable"
    else:
        return f"{name}: Bad"

# Execute the main function
main()
