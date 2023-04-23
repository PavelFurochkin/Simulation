from abc import abstractmethod
from collections import deque

from map.coordinates import Coordinates

from instance_of_the_world.aliveentity import AliveEntity


class Creature(AliveEntity):
    def __init__(self, coordinates, speed: int, health: int, sprite: str,
                 fight_power):
        super().__init__(coordinates, sprite, health)
        self.speed = speed
        self.fight_power = fight_power

    def make_move(self, map, entity: AliveEntity, path: deque) -> None:
        # Делаем ход, если рядом нет цели
        if path is not None and len(path) > 1:
            for move in range(self.speed):
                if len(path) > 1:
                    step = path.popleft()
                    print(f'{entity.sprite} сходил')
                    print(f'({entity.coordinates.row};'
                          f'{entity.coordinates.column})---->'
                          f'({Coordinates(step[0], step[1]).row};'
                          f'{Coordinates(step[0], step[1]).column})')
                    map.move_object(entity, entity.coordinates,
                                    Coordinates(step[0], step[1]))
            # Если на клетке допустимое существо - взаимодействуем
        elif path is not None:
            _pray_coordinate = path.popleft()
            _pray = map.get_object(
                Coordinates(_pray_coordinate[0], _pray_coordinate[1])
            )
            self._meeting(map, entity, _pray)
            print(f'{entity.sprite}'
                  f'({entity.coordinates.row};'f'{entity.coordinates.column})'
                  f' атаковал '
                  f'{_pray.sprite}'
                  f'({_pray.coordinates.row};'f'{_pray.coordinates.column})')
        else:
            pass

    @abstractmethod
    def _meeting(self, map, first_entity, second_entity) -> None:
        """
        Базовый метод взаимодействия представителей пищевых цепочек
        """
        pass