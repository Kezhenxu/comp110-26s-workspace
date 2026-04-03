"""File to define River class."""

from __future__ import annotations
from .fish import Fish
from .bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int) -> None:
        self.fish = self.fish[amount:]

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self):
        for _ in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())

    def repopulate_bears(self):
        for _ in range(len(self.bears) // 2):
            self.bears.append(Bear())

    def __str__(self) -> str:
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, other_riv: River) -> River:
        total_fish = len(self.fish) + len(other_riv.fish)
        total_bears = len(self.bears) + len(other_riv.bears)
        return River(total_fish, total_bears)

    def __mul__(self, factor: int) -> River:
        total_fish = len(self.fish) * factor
        total_bears = len(self.bears) * factor
        return River(total_fish, total_bears)

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()
