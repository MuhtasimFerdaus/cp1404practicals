"""
CP1404/CP5632 - Practical
Calculates total price for a number of items.
Applies a 10% discount if total exceeds $100.
Ensures number of items is non-negative.
"""

# Input validation for the number of items
num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

# Initialize the total price
total_price = 0

# Loop to get the price for each item
for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply a 10% discount if the total price exceeds $100
if total_price > 100:
    total_price *= 0.9

# Display the total price, formatted to 2 decimal places
print(f"Total price for {num_items} items is ${total_price:.2f}")