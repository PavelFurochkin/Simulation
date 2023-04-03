from instance_of_the_world.entitys import Entity


class Rock(Entity):

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.SPEAD: int = 0
        self.health: int = 1000
        self.sprite = 'Rc'

