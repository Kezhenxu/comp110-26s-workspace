"""Unit tests for dictionary utility functions."""

__author__ = "730873961"

import pytest
from exercises.EX05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


def test_invert_use_case1() -> None:
    """Test invert with multiple unique key-value pairs."""
    assert invert({"a": "x", "b": "y", "c": "z"}) == {
        "x": "a",
        "y": "b",
        "z": "c",
    }


def test_invert_use_case2() -> None:
    """Test invert with one key-value pair."""
    assert invert({"apple": "red"}) == {"red": "apple"}


def test_invert_edge_case() -> None:
    """Test invert raises KeyError when duplicate values exist."""
    with pytest.raises(KeyError):
        invert({"alyssa": "byrnes", "adam": "byrnes"})


def test_favorite_color_use_case1() -> None:
    """Test favorite_color returns the most frequent color."""
    assert favorite_color({"Max": "blue", "Sarah": "red", "Tina": "blue"}) == "blue"


def test_favorite_color_use_case2() -> None:
    """Test favorite_color with only one entry."""
    assert favorite_color({"Max": "green"}) == "green"


def test_favorite_color_edge_case() -> None:
    """Test favorite_color returns empty string for empty dictionary."""
    assert favorite_color({}) == ""


def test_count_use_case1() -> None:
    """Test count with repeated values."""
    assert count(["apple", "banana", "apple", "apple"]) == {
        "apple": 3,
        "banana": 1,
    }


def test_count_use_case2() -> None:
    """Test count with all unique values."""
    assert count(["red", "blue", "green"]) == {
        "red": 1,
        "blue": 1,
        "green": 1,
    }


def test_count_edge_case() -> None:
    """Test count with an empty list."""
    assert count([]) == {}


def test_alphabetizer_use_case1() -> None:
    """Test alphabetizer groups words by first letter."""
    assert alphabetizer(["cat", "apple", "car", "banana"]) == {
        "c": ["cat", "car"],
        "a": ["apple"],
        "b": ["banana"],
    }


def test_alphabetizer_use_case2() -> None:
    """Test alphabetizer handles uppercase starting letters."""
    assert alphabetizer(["Zebra", "zoo", "Apple"]) == {
        "z": ["Zebra", "zoo"],
        "a": ["Apple"],
    }


def test_alphabetizer_edge_case() -> None:
    """Test alphabetizer skips words that do not start with a letter."""
    assert alphabetizer(["1dog", "!wow", "apple"]) == {"a": ["apple"]}


def test_update_attendance_use_case1() -> None:
    """Test update_attendance adds a student to an existing day."""
    attendance = {"Monday": ["Alice", "Bob"]}
    update_attendance(attendance, "Monday", "Charlie")
    assert attendance == {"Monday": ["Alice", "Bob", "Charlie"]}


def test_update_attendance_use_case2() -> None:
    """Test update_attendance creates a new day when needed."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Tuesday", "Bob")
    assert attendance == {
        "Monday": ["Alice"],
        "Tuesday": ["Bob"],
    }


def test_update_attendance_edge_case() -> None:
    """Test update_attendance allows duplicate student names."""
    attendance = {"Monday": ["Alice", "Bob"]}
    update_attendance(attendance, "Monday", "Alice")
    assert attendance == {"Monday": ["Alice", "Bob", "Alice"]}
