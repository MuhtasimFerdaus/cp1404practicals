"""
CP1404/CP5632 Practical
Hexadecimal colour codes based on colour names
"""
COLOUR_TO_HEX = {
    "Aliceblue": "#f0f8ff", "Antiquewhite": "#faebd7", "Aqua": "#00ffff", "Beige": "#f5f5dc", "Coral": "#ff7f50", "Crimson": "#dc143c", "Darkolivegreen": "#556b2f", "Gold": "#ffd700", "Hotpink": "#ff69b4", "Ivory": "#fffff0"
}
print("All colour names and corresponding hex codes:")
for colour, hex_code in COLOUR_TO_HEX.items():
    print(f"{colour:15} is {hex_code}")

colour_name = input("Enter colour name: ").capitalize()

while colour_name != "":
    try:
        print(f"Hexadecimal for {colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except StopIteration:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").capitalize()

