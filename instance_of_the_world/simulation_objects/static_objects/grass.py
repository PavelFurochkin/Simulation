from instance_of_the_world.entitys import Entity


class Grass(Entity):

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.SPEAD: int = 0
        self.health: int = 100
        self.sprite = 'Gr'
