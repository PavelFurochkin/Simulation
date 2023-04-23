from instance_of_the_world import Herbivore
from instance_of_the_world.creatures import Creature
from map.coordinates import Coordinates


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, spead: int = 3,
                 health: int = 10, fight_power: int = 6, sprite='Pr'):
        super().__init__(coordinates, spead, health, sprite, fight_power)
        self.successful_hunting: int = 0

    def _meeting(self, map, first_entity: Creature,
                 second_entity: Creature) -> None:
        """
        Метод моделирует взаимодействие представителей пищевых цепочек
        """
        if (isinstance(first_entity, Predator) and
                isinstance(second_entity, Herbivore)):
            second_entity.health -= first_entity.fight_power  # Хищник нападает на травоядное
            first_entity.health += 2
            if second_entity.health <= 0:
                map.delete(second_entity.coordinates)

        else:
            print('Взаимодействие невозможно')