from collections import deque

from action.PathFinding.CurrentNode import Node
from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates
from map.maps import Map


class FindPath:
    """
    Класс для поиска пути на карте

    ...

    Attribute
    ---------
    self.__hunter: Entity
        содержит тип существа - охотника
    self.__pray: Entity
        содержит тип существа - "жертвы"
    self.__field: Map
        содержит актуальную карту
    self.__visited_spot: set
        список посещенных клеток
    self.__neighbours_queue: deque
        содержит очередь клеток которые нужно посетить.

    Methods
    -------
    finding_path(self)
        метод позволяет найти путь до цели,
        проверяя на соотвествие соседних клеток с клеткой цели,
        также добавляет пустые клетки в список посещенных.

    filling_queue(self, spot: Coordinates)
        метод для наполнения очереди непосещенных клеток.
    """

    def __init__(self, hunter: Entity = None,
                 pray: Entity = None, field: Map = None):
        self.__hunter: Entity = hunter
        self.__pray: Entity = pray
        self.__field: Map = field
        self.__visited_spot = set()
        self.__neighbours_queue = deque()

        __coordinated = Node(self.__field, Coordinates(self.__hunter.coordinates.row,
                                                       self.__hunter.coordinates.column))
        self.__neighbours_queue.append(__coordinated)

    def finding_path(self):
        '''
        Метод для поиска пути от охотника до цели
        :return:
        '''
        while True:
            if len(self.__neighbours_queue) > 0:
                # Берем крайний левый адрес из очереди
                self.__actual_node = self.__neighbours_queue.popleft()
                self.__visited_spot.add(self.__actual_node)
                # Проверяем что выбранная клетка является жертвой
                if (self.__field.get_object(self.__actual_node.row,
                                            self.__actual_node.column).sprite
                        == self.__pray.sprite):
                    Node(self.__field, self.__actual_node).create_path(
                        Node(self.__field, self.__actual_node))
                    # Если клетка пустая, то добавляем в очередь
                elif (self.__field.spot_is_empty(
                        Coordinates(self.__actual_node.row,
                                    self.__actual_node.column))):
                    self.filling_queue(self.__actual_node)

    def filling_queue(self, spot: Coordinates):
        nodes = Node(self.__field, spot).extend_node()
        for node in nodes:
            if (node not in self.__visited_spot and
                    self.__field.spot_is_empty(node)):
                self.__neighbours_queue.append(node)
            elif (isinstance(type(self.__field.spot_is_empty(node)),
                             type(self.__pray))):
                self.__neighbours_queue.append(node)
                break
