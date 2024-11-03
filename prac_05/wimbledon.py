"""
CP1404/CP5632 Practical
Wimbledon data-reading, processing, and displaying
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip the header line
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        country = record[INDEX_COUNTRY]
        champion = record[INDEX_CHAMPION]

        countries.add(country)

        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} : {count}")

    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

main()
