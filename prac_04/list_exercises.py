def main():
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
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

main()
