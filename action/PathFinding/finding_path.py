from collections import deque
from typing import TypeVar, Type

from action.PathFinding.currentNode import Node
from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates
from map.maps import Map
from render.render import RenderField


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
                 pray=None, field: Map = None):
        self.__hunter: Entity = hunter
        self.__pray: Type[Entity] = pray
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
        RenderField().render(self.__field)
        tray = 0
        while True:
            if len(self.__neighbours_queue) > 0:
                # Берем крайний левый адрес из очереди
                self.__actual_node = self.__neighbours_queue.popleft()
                self.__visited_spot.add(self.__actual_node)

                # Если клетка пустая, то добавляем в очередь
                if (self.__field.spot_is_empty(
                    Coordinates(self.__actual_node.row,
                                self.__actual_node.column)) or tray == 0):
                    self.filling_queue(self.__actual_node)
                    tray += 1
                # Проверяем что выбранная клетка является жертвой
                elif (self.__field.get_object(self.__actual_node.row,
                                              self.__actual_node.column).sprite
                        == self.__pray.sprite):
                    self.filling_queue(self.__actual_node)
                    path: deque = (self.__actual_node.
                                   create_path(self.__actual_node))
                    return path

    def filling_queue(self, spot: Node):
        nodes = spot.extend_node()
        for node in nodes:
            if (node not in self.__visited_spot and
                    self.__field.spot_is_empty(node)):
                self.__neighbours_queue.append(node)
            elif (isinstance(type(self.__field.spot_is_empty(node)),
                             type(self.__pray))):
                self.__neighbours_queue.append(node)
                break
