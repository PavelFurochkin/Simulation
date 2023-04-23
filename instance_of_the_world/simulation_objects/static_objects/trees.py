from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates


class Tree(Entity):
    def __init__(self, coordinates: Coordinates, sprite='Tr'):
        super().__init__(coordinates, sprite)
