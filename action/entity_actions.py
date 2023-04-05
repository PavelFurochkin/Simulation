from instance_of_the_world.simulation_objects.static_objects import Grass, Tree, Rock
from instance_of_the_world.simulation_objects.dinamic_objects import Herbivore, Predator
from instance_of_the_world.entitys import Entity
from action.selection_of_action import Selection
from map.coordinates import Coordinates
from map.maps import Map


class Actions:

    def __init__(self, map: Map):
        self.field = map

    def make_move(self, entity: Entity, digit: int):
        # Выбираем клетку для взаимодействия
        select_position = Selection(entity.coordinates)
        if 0 <= digit <= 7:  # Диапазон соседних клеток для перемещения
            # Перешагиваем на новую клетку
            self.coordinates = select_position.interact(digit)
        if 8 <= digit <= 15:  # Диапазон соседних клеток для атаки
            # Выбираем клетку для взаимодействия
            select_position = Selection(entity.coordinates)
            # Выбираем соседнюю клетку для атаки
            attack_sprite: tuple = select_position.interact(digit)
            # Проверяем что клетка не пустая
            target_entity = self.field.spot_is_empty(Coordinates(*attack_sprite))
            # Если на клетке допустимое существо - взаимодействуем
            if (target_entity is not None and
                    not isinstance(target_entity, Rock)):
                self.meeting(entity, target_entity)

    def meeting(self, first_entity: Entity, second_entity: Entity) -> None:
        """
        Метод моделирует взаимодействие представителей пищевых цепочек
        """
        if (first_entity is isinstance(first_entity, Predator) and
                second_entity is isinstance(second_entity, Herbivore)):
            second_entity.health -= 2  # Хищник нападает на травоядное
            first_entity.health += 2
            if second_entity.health == 0:
                self.field.delete(second_entity.coordinates)

        elif (first_entity is isinstance(first_entity, Herbivore) and
              second_entity is isinstance(second_entity, (Grass, Tree))):
            second_entity.health -= 5  # Травоядное ест траву
            first_entity.health += 2
            if second_entity.health == 0:
                self.field.delete(second_entity.coordinates)

        elif (first_entity is isinstance(first_entity, Predator)
                and second_entity is isinstance(second_entity, Predator)
                and (first_entity and second_entity).successful_hunting > 3
                and first_entity.gender != second_entity.gender):
            self.field.add(Entity().set_start_position(), first_entity)

        elif (first_entity is isinstance(first_entity, Herbivore)
                and second_entity is isinstance(second_entity, Herbivore)
                and first_entity.gender != second_entity.gender):
            self.field.add(Entity().set_start_position(), first_entity)

        else:
            print('Взаимодействие невозможно')
