from action.Coordinates import Coordinates
from action.SelectionOfAction import Selection
from map import Map

from instanceOfTheWorld.Creature import Creature
from instanceOfTheWorld.Hearvibore import Hearvibore


class Predator(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 spead: int = 3, health: int = 10, fight_power: int = 2):
        super().__init__(coordinates, spead, health)
        self.health = health
        self.spead = spead
        self.fight_power: int = fight_power

    def make_move(self, digit: int):
        super().make_move(digit)
        if 9 <= digit <= 16:  # Диапазон соседних клеток для атаки
            select_position = Selection(self.coordinates)  # Выбираем клетку для взаимодействия
            attack_sprite: tuple = select_position.interact(digit)  # Выбираем соседнюю клетку для атаки
            target_entity = Map.checkSpotNotEmpty(*attack_sprite)  # Проверяем что клетка не пустая
            if target_entity is not None and isinstance(target_entity, Hearvibore):  # Если на клетке травоядное атакуем
                Map.meeting(self, target_entity)
            else:
                pass



