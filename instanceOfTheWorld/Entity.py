from abc import ABC
from random import randint

from action.Coordinates import Coordinates


class Entity(ABC):
    quantity: int = 0  # Количество объектов на поле

    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0)):
        self.coordinates = coordinates
        # self.identifier = id(self)

    def set_start_position(self):
        self.coordinates = Coordinates(row=randint(1, 20),
                                       column=randint(1, 20))
