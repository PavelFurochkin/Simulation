from abc import ABC

from map.coordinates import Coordinates


class Entity(ABC):
    def __init__(self, coordinates: Coordinates, sprite: str):
        self.coordinates = coordinates
        self.sprite = sprite
