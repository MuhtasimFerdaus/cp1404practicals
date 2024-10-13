import random

# Constants
MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_QUICK_PICK = 6

def main():
    # Ask the user how many quick picks they wish to generate
    number_of_picks = int(input("How many quick picks? "))

    # Generate the required number of quick picks
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    #Generate a single quick pick of 6 unique random numbers between 1 and 45.
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_QUICK_PICK:
        number = random.randint(MINIMUM, MAXIMUM)  # Generate a random number
        if number not in quick_pick:  # Ensure the number is not already in the list
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def print_quick_pick(quick_pick):
    #Print the quick pick in a formatted way.
    # Print each number in the quick pick, formatted with 2 spaces
    print(" ".join(f"{number:2}" for number in quick_pick))


main()
