try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero. Please enter again.")
        denominator = int(input("Enter denominator: "))

    fraction = numerator / denominator
    print(f"Result: {fraction}")

except ValueError:
    print("Invalid input! Please enter integers only.")

print("Finished.")