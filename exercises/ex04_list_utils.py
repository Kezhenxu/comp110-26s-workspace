"""exercises.ex04_list_utils"""

__author__ = "730873961"


def all(numbers: list[int], value: int) -> bool:
    """Return True if all elements in numbers equal value, False otherwise."""

    if len(numbers) == 0:
        return False

    for num in numbers:
        if num != value:
            return False

    return True


def max(input: list[int]) -> int:
    """Return the largest integer in input. Raise ValueError if empty."""

    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    largest = input[0]

    for i in input:
        if i > largest:
            largest = i

    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if list1 and list2 have the same length and same items at each index."""

    if len(list1) != len(list2):
        return False

    idx: int = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:

    idx: int = 0
    while idx < len(list2):
        list1.append(list2[idx])
        idx += 1
