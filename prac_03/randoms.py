import random

# Random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # Line 1

# Random odd number between 3 and 9 (inclusive)
print(random.randrange(3, 10, 2))  # Line 2

# Random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # Line 3

# Generating a random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")