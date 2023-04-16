from collections import deque
from typing import List

from map.coordinates import Coordinates
from map.maps import Map


class Node:
    """
    Класс представляет клеку на карте
    ...
    Attribute
    ---------
    map: Map
        представляет карту актуальную карту
    point: Coordinates
        представляет координаты клетки
    parent: Node
        представляет родителя текущей клетки

    Methods
    ------
    extend_node(self)
        описывает метод добавления соседних клеток
    create_path(self, final_node)
        строит путь от охотника до жертвы
    """

    def __init__(self, map: Map, point: Coordinates):
        self.point = point
        self.__map = map
        self.__parent = None

    def extend_node(self) -> List:
        """
        Добавляет в список соседние от целевой клетки
        :param
        ------
        neighbours_node: List[tuple]
            Список  координат соседних клеток
        children: List
            пустой список для добавления координат соседних клеток
        :return
        -------
        List
            список доступных соседних клеток
        """
        neighbours_node: List[tuple] = [
            (-1, -1), (0, -1), (1, -1), (1, 0),
            (1, 1), (0, 1), (-1, 1), (-1, 0)  # Список соседних клеток, с которыми можем взаимодействовать
        ]
        children: List = []
        for neighbour in neighbours_node:
            if ((0 < self.point.row + neighbour[0] < self.__map.row_map + 1) and
                    (0 < self.point.column + neighbour[1] < self.__map.column_map + 1)):
                right_neighbor = Node(self.__map,
                                      (Coordinates(self.point.row + neighbour[0],
                                                   self.point.column + neighbour[1]))
                                      )
                children.append(right_neighbor)
        for child in children:
            child.__parent = self
        return children

    def create_path(self, final_node) -> deque:
        """
        Добавляет в список путь от заданной точки до цели и инвертирует его
        :param
        final_node: клетка с местоположением цели
        :return: список координат до цели
        """
        path = deque()
        current_node = final_node
        while current_node.__parent is not None:
            path.insert(0, (current_node.point.row, current_node.point.column))
            current_node = current_node.__parent
        path.insert(0, (current_node.point.row, current_node.point.column))
        path.popleft()
        return path

    def __eq__(self, other):
        return self.point == other.point

    def __hash__(self):
        return hash(self.point)