"""
CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class
Approximate time: 40 mins
"""

from prac_06.programming_language import ProgrammingLanguage

# Create instances of ProgrammingLanguage for each language
java = ProgrammingLanguage("Java", "Static", True, 1995)
cpp = ProgrammingLanguage("C++", "Static", False, 1983)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

# Create a list of ProgrammingLanguage objects
languages = [java, cpp, python, visual_basic, ruby]

# Print the list to verify it contains the correct objects
for lang in languages:
    print(lang)


# Loop through and print the names of all languages with dynamic typing
print("Languages with dynamic typing:")
for lang in languages:
    if lang.is_dynamic():  # Check if the language is dynamically typed
        print(lang.name)