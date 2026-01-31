"""exercises.ex01_tea_party"""

__author__ = "730873961"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    """tell user to enter a word that should be exactly 5 characters long"""

    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    """check whether the word is 5-character long"""

    return word


"""return the valid word"""


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    """tell user to enter a single character"""

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    """check the length of letter"""

    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)

    count: int = 0
    """Initialize a variable - counter"""

    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    """Check each index of the 5-character word individually"""

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)
    """After checking all indices, print a summary message"""


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


"""entry point of the program, gathers valid input"""


if __name__ == "__main__":
    main()
"""makes it possible to run Python program as a module"""
