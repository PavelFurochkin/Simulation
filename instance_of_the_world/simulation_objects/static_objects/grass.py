from dataclasses import dataclass

from instance_of_the_world.entitys import Entity


@dataclass(frozen=True)
class Grass(Entity):
    SPEAD: int = 0
    health: int = 100
