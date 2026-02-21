"""exercises.ex03_wordle"""

__author__ = "730873961"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user for a guess of exactly secret_word_len characters."""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Return True if char_guess is found anywhere in secret_word."""

    assert len(char_guess) == 1

    index: int = 0

    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1

    return False


WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def emojified(guess: str, secret: str) -> str:
    """Return a string of emojis representing how guess compares to secret."""

    assert len(guess) == len(secret)

    result: str = ""
    index: int = 0

    while index < len(secret):

        if guess[index] == secret[index]:
            result += GREEN_BOX

        elif contains_char(secret_word=secret, char_guess=guess[index]):
            result += YELLOW_BOX

        else:
            result += WHITE_BOX

        index += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = False

    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")

        guess: str = input_guess(secret_word_len=len(secret))
        print(emojified(guess=guess, secret=secret))

        if guess == secret:
            won = True
        else:
            turn += 1

    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
