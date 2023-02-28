from typing import List

from action.Coordinates import Coordinates


class Selection:
    """
    В классе представленны варианты при выборе хода и их случайная генерация
    """
    def __init__(self, position: Coordinates):
        self.x, self.y = position

    def interact(self, digit: int) -> tuple:
        directions: List[tuple] = [
            (-1, -1), (0, -1), (1, -1), (1, 0),
            (1, 1), (0, 1), (-1, 1), (-1, 0)  # Список соседних клеток, с которыми можем взаимодействовать
        ]
        dx, dy = directions[digit % 8]
        x, y = self.x + dx, self.y + dy
        return (x, y)
