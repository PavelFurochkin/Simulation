from dataclasses import dataclass

from instanceOfTheWorld.Entity import Entity


@dataclass(frozen=True)
class Tree(Entity):
    SPEAD: int = 0
    health: int = 500
