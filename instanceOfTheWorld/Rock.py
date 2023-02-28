from dataclasses import dataclass

from instanceOfTheWorld.Entity import Entity


@dataclass(frozen=True)
class Rock(Entity):
    SPEAD: int = 0
    HEALTH: int = 1000
