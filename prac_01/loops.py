"""
CP1404/CP5632 - Practical
Demonstrates looping in Python with various tasks:
1. Displays odd numbers from 1 to 20.
2. Counts by tens from 0 to 100.
3. Counts down from 20 to 1.
4. Prints a user-defined number of stars on one line.
5. Prints lines of increasing stars based on user input.
"""
# Display all the odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars. Ask the user for a number, then print that many stars (*), all on one line.
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

# d. Print n lines of increasing stars.
print("Lines of increasing stars")
for i in range(1, n + 1):
    print('*' * i)