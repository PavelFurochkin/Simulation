from collections import deque

from action.PathFinding.currentNode import Node
from instance_of_the_world.entitys import Entity
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
                 pray=None, field: Map = None) -> None:
        self.__hunter: Entity = hunter
        self.__pray_class = pray
        self.__field: Map = field
        self.__visited_spot = set()
        self.__neighbours_queue = deque()

        __coordinated = Node(self.__field, self.__hunter.coordinates)
        self.__neighbours_queue.append(__coordinated)

    def finding_path(self) -> deque:
        '''
        Метод для поиска пути от охотника до цели
        :return:
        '''
        tray = 0
        while True:
            if len(self.__neighbours_queue) > 0:
                # Берем крайний левый адрес из очереди
                self.__actual_node = self.__neighbours_queue.popleft()
                self.__visited_spot.add(self.__actual_node)
                actual_object = self.__field.get_object(self.__actual_node.point)

                # Если клетка пустая, то добавляем в очередь
                if (self.__field.spot_is_empty(self.__actual_node.point) or tray == 0):
                    self.filling_queue(self.__actual_node)
                    tray += 1
                # Проверяем что выбранная клетка является жертвой
                elif isinstance(actual_object, self.__pray_class):
                    self.filling_queue(self.__actual_node)
                    path: deque = (self.__actual_node.
                                   create_path(self.__actual_node))
                    return path

    def filling_queue(self, spot: Node) -> None:
        nodes = spot.extend_node()
        for node in nodes:
            if (node not in self.__visited_spot and
                    self.__field.spot_is_empty(node)):
                self.__neighbours_queue.append(node)
            elif (isinstance(type(self.__field.get_object(node.point)),
                             type(self.__pray_class))):
                self.__neighbours_queue.append(node)
                break
