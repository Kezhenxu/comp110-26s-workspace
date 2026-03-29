"""exercises.ex05_dictionary"""

__author__ = "730873961"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary with keys and values swapped."""
    result: dict[str, str] = {}

    for key in d:
        value = d[key]

        if value in result:
            raise KeyError("Duplicate key when inverting")

        result[value] = key

    return result


def favorite_color(names_colors: dict[str, str]) -> str:
    """Return the color that appears most frequently in the dictionary."""
    count: dict[str, int] = {}

    for name in names_colors:
        color = names_colors[name]

        if color in count:
            count[color] += 1
        else:
            count[color] = 1

    favorite = ""
    max_count = 0

    for color in count:
        if count[color] > max_count:
            favorite = color
            max_count = count[color]

    return favorite


def count(values: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each value appears."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by their starting letter in a dictionary."""
    result: dict[str, list[str]] = {}

    for word in words:
        if not word[0].isalpha():
            continue

        letter = word[0].lower()

        if letter not in result:
            result[letter] = []

        result[letter].append(word)

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Add a student's attendance to the given day in the dictionary."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
