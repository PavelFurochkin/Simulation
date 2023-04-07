from abc import ABC
from random import randint

from map.coordinates import Coordinates


class Entity(ABC):
    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 sprite=' '):
        self.coordinates = coordinates
        self.sprite = sprite
        self.spead = 0
