import csv
from guitar import Guitar  # Importing the Guitar class from guitar.py

FILENAME = "guitars.csv"

def main():
    """Main function to load, display, sort, add, and save guitars."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    # Sort guitars by year (oldest to newest) using the __lt__ method in Guitar
    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)

    # Add new guitars from user input
    add_new_guitars(guitars)

    # Save updated list to the CSV file
    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
    return guitars

def display_guitars(guitars):
    """Display all guitars in the list."""
    if not guitars:
        print("No guitars to display.")
    else:
        for i, guitar in enumerate(guitars, 1):
            print(f"{i}. {guitar}")

def add_new_guitars(guitars):
    """Prompt the user to add new guitars."""
    print("\nAdd new guitars (enter a blank name to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar} added.")
        except ValueError:
            print("Invalid input. Please enter valid numeric values for year and cost.")

def save_guitars(filename, guitars):
    """Save all guitars to a file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()

