from prac_06.guitar import Guitar


def main():
    print("My guitars!")

    # List to hold the guitar objects
    guitars = []

    # Uncomment this section for user input
    # while True:
    #     name = input("Name: ")
    #     if name == "":
    #         break  # Exit the loop if the name is blank
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))

    #     # Create a Guitar object and add it to the list
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print(f"{guitar} added.")

    # Test Data
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        # Use ternary operator for vintage check
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        # Print formatted output
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
