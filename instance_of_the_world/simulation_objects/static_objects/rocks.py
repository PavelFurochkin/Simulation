from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates


class Rock(Entity):
    def __init__(self, coordinates: Coordinates, sprite='Rc'):
        super().__init__(coordinates, sprite)
