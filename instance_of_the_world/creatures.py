from instance_of_the_world.entitys import Entity


class Creature(Entity):
    def __init__(self, coordinates, spead: int, health: int):
        super().__init__(coordinates)
        self.spead = spead
        self.health = health


