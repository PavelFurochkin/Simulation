from instance_of_the_world.creatures import Creature
from map.coordinates import Coordinates


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, spead: int = 5,
                 health: int = 12, fight_power: int = 2, sprite='Hb'):
        super().__init__(coordinates, spead, health, sprite, fight_power)

    def _meeting(self, map, first_entity: Creature,
                 second_entity) -> None:
        """
        Метод моделирует взаимодействие представителей пищевых цепочек
        """
        second_entity.health -= first_entity.fight_power  # Травоядное ест траву
        first_entity.health += 2
        if second_entity.health <= 0:
            map.delete(second_entity.coordinates)

        else:
            print('Взаимодействие невозможно')
