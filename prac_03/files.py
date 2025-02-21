# Writing user’s name to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Reading the name from the file
with open("name.txt", "r") as file:
    stored_name = file.read().strip()
print(f"Hi {stored_name}!")

# Writing numbers to a file
with open("numbers.txt", "w") as file:
    file.write("17\n42\n400\n")

# Reading first two numbers and adding them
with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
print(f"Sum of first two numbers: {num1 + num2}")

# Summing all numbers in the file
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(f"Total sum: {total}")