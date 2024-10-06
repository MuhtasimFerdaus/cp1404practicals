"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# Get the sales input from the user
sales = float(input("Enter sales: $"))

# Continue processing while the sales value is greater than 0
while sales > 0:
    # Check if sales are less than $1,000 and apply the corresponding bonus
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus
    else:
        bonus = sales * 0.15  # 15% bonus

    # Display the calculated bonus
    print(f"Your bonus is: ${bonus:.2f}")

    # Ask for the next sales input (the loop will stop if the user enters 0 or less)
    sales = float(input("Enter sales: $"))
print(f"NO bonus for sales of ${sales}")

