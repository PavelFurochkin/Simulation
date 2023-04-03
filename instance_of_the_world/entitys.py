from abc import ABC
from random import randint

from map.coordinates import Coordinates


class Entity(ABC):
    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0)):
        self.coordinates = coordinates
        self.sprite = ' '

    def set_start_position(self) -> Coordinates:
        self.coordinates = Coordinates(row=randint(1, 20), column=randint(1, 20))
        return Coordinates(self.coordinates.row, self.coordinates.column)