from typing import List

from map.coordinates import Coordinates


class Selection:
    """
    В классе представленны варианты при выборе хода и их случайная генерация
    """
    __STEP = 8
    def __init__(self, position: Coordinates):
        self.__x = position.row
        self.__y = position.column

    def interact(self, digit: int) -> tuple:
        directions: List[tuple] = [
            (-1, -1), (0, -1), (1, -1), (1, 0),
            (1, 1), (0, 1), (-1, 1), (-1, 0)  # Список соседних клеток, с которыми можем взаимодействовать
        ]
        dx, dy = directions[digit % self.__STEP]
        x, y = self.__x + dx, self.__y + dy
        return (x, y)

