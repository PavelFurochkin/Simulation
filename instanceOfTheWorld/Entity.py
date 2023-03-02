from abc import ABC
from random import randint

import action.Coordinates as Coordinates


class Entity(ABC):
    quantity: int = 0  # Количество объектов на поле

    def __init__(self, coordinates: Coordinates = Coordinates.Coordinates(row=0, column=0)):
        self.coordinates = coordinates
        # self.identifier = id(self)

    def set_start_position(self):
        self.coordinates = Coordinates.Coordinates(row=randint(1, 20),
                                                   column=randint(1, 20))
