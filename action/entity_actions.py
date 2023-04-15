from collections import deque
from time import sleep

from instance_of_the_world.simulation_objects.static_objects import Grass, Rock
from instance_of_the_world.simulation_objects.dinamic_objects import Herbivore, Predator
from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates
from map.maps import Map
from render.render import RenderField


class Action:

    def __init__(self, map: Map):
        self.field = map

    def make_move(self, entity: Entity, path: deque) -> None:
        # Делаем ход, если рядом нет цели
        if len(path) > 1:
            for move in range(entity.spead):
                if len(path) > 1:
                    step = path.popleft()
                    self.field.move_object(entity,
                                           entity.coordinates,
                                           Coordinates(step[0], step[1]))
                    sleep(1)
                    print('------------------')
                    RenderField().render(self.field)

            # Если на клетке допустимое существо - взаимодействуем
        elif not isinstance(entity, Rock):
            _pray_coordinate = path.popleft()
            _pray = self.field.get_object(
                Coordinates(_pray_coordinate[0], _pray_coordinate[1])
            )
            self.__meeting(entity, _pray)
            RenderField().render(self.field)
            print(f'{entity.sprite} атаковал {_pray.sprite}')

    def __meeting(self, first_entity: Entity, second_entity: Entity) -> None:
        """
        Метод моделирует взаимодействие представителей пищевых цепочек
        """
        if (isinstance(first_entity, Predator) and
                isinstance(second_entity, Herbivore)):
            second_entity.health -= 2  # Хищник нападает на травоядное
            first_entity.health += 2
            # first_entity.successful_hunting += 1 # Нереализованная механика при наличии размножения
            if second_entity.health <= 0:
                self.field.delete(second_entity.coordinates)

        elif (isinstance(first_entity, Herbivore) and
              isinstance(second_entity, Grass)):
            second_entity.health -= 5  # Травоядное ест траву
            first_entity.health += 2
            if second_entity.health <= 0:
                self.field.delete(second_entity.coordinates)


        # Нереализованная механика при наличии размножения
        # elif (first_entity is isinstance(first_entity, Predator)
        #         and second_entity is isinstance(second_entity, Predator)
        #         and (first_entity or second_entity).successful_hunting >= 3
        #         and first_entity.gender != second_entity.gender):
        #     SpawnEntity(self.field).add_to_map(first_entity, randint(1, 3))
        #     first_entity.successful_hunting = 0
        #     second_entity.successful_hunting = 0
        #
        # elif (first_entity is isinstance(first_entity, Herbivore)
        #         and second_entity is isinstance(second_entity, Herbivore)
        #         and first_entity.gender != second_entity.gender):
        #     SpawnEntity(self.field).add_to_map(first_entity, randint(1, 3))

        else:
            print('Взаимодействие невозможно')

    # Нереализованная механика охоты при наличии размножения
    # def choose_a_pray(self, hunting_list: list, map: Map):
    #     shortest_way: int = 1000
    #     self.preferred_entity = None
    #     new_hunting_list = hunting_list.copy()
    #     for index_en, entity in enumerate(new_hunting_list):
    #         if isinstance(entity, Predator):
    #             if entity.successful_hunting >= 3:
    #                 for index_partner, partner in enumerate(new_hunting_list):
    #                     if isinstance(partner, Predator):
    #                         path = FindPath(entity, partner, map).finding_path()
    #                         if len(path) < shortest_way:
    #                             self.preferred_entity = partner
    #                             new_hunting_list.pop(index_partner)
    #             else:
    #                 for index_pray, pray in enumerate(new_hunting_list):
    #                     if isinstance(pray, Herbivore):
    #                         path = FindPath(entity, pray, map).finding_path()
    #                         if len(path) < shortest_way:
    #                             self.preferred_entity = pray
    #                             new_hunting_list.pop(index_pray)
    #         if isinstance(entity, Herbivore):
    #             for index_pray, pray in enumerate(new_hunting_list):
    #                 if isinstance(pray, (Grass, Tree)):
    #                     path = FindPath(entity, pray, map).finding_path()
    #                     if len(path) < shortest_way:
    #                         self.preferred_entity = pray
    #                         new_hunting_list.pop(index_pray)
    #     return self.preferred_entity