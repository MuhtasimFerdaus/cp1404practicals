"""CP1404/CP5632 Practical - ProgrammingLanguage class."""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

        name: str, the name of the programming language
        typing: str, the typing discipline (Static or Dynamic)
        reflection: str, whether the language supports reflection (Yes or No)
        year: int, the year the language was first released
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, else False."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
