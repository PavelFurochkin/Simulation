from abc import ABC, abstractmethod
from dataclasses import dataclass


class Entity(ABC):

    @abstractmethod
    def draw_start_position(self):
        pass


@dataclass(frozen=True)
class Rock(Entity):
    spead: int = 0
    health: int = 1

    def draw_start_position(self):
        return 'R'


@dataclass(frozen=True)
class Grass(Entity):
    spead: int = 0
    health: int = 1

    def draw_start_position(self):
        pass


@dataclass(frozen=True)
class Tree(Entity):
    spead: int = 0
    health: int = 1

    def draw_start_position(self):
        pass


@dataclass()
class Creature(Entity,ABC):
    spead: int
    health: int

    def draw_start_position(self):
        pass


    @abstractmethod
    def make_move(self):
        pass

    @abstractmethod
    def search_for_food(self):
        pass

class Hearvibore(Creature):

    def draw_start_position(self):
        pass


    def make_move(self):
        pass


    def search_for_food(self):
        pass


@dataclass()
class Predator(Creature):
    fight_power: int

    def draw_start_position(self):
        pass


    def make_move(self):
        pass


    def search_for_food(self):
        pass


f = Hearvibore(1, 1)
print(f)