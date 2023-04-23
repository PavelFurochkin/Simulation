from map.coordinates import Coordinates

from instance_of_the_world.entitys import Entity


class AliveEntity(Entity):
    def __init__(self, coordinates: Coordinates, sprite: str, health):
        super().__init__(coordinates, sprite)
        self.health = health
