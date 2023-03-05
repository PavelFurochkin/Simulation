from dataclasses import dataclass

from instance_of_the_world.entitys import Entity


@dataclass(frozen=True)
class Rock(Entity):
    SPEAD: int = 0
    HEALTH: int = 1000
