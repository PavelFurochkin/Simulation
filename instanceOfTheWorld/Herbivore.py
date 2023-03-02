import action.Coordinates as Coordinates
import action.SelectionOfAction as Selection

import instanceOfTheWorld.Creature as Creature
import instanceOfTheWorld.Grass as Grass
import instanceOfTheWorld.Map as Map


class Hearvibore(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates.Coordinates(row=0, column=0),
                 spead: int = 5, health: int = 20):
        super().__init__(coordinates, spead, health)
        self.health = health
        self.spead = spead

    def make_move(self, digit: int):
        super().make_move(digit)
        if 9 <= digit <= 16:  # Диапазон соседних клеток для атаки
            select_position = Selection.Selection(self.coordinates)  # Выбираем клетку для взаимодействия
            attack_sprite: tuple = select_position.interact(digit)  # Выбираем соседнюю клетку для атаки
            target_entity = Map.Map.checkSpotNotEmpty(*attack_sprite)  # Проверяем что клетка не пустая
            if target_entity is not None and isinstance(target_entity, Grass.Grass):  # Если на клетке травоядное атакуем
                # Map.meeting(self, target_entity)
                pass
            else:
                pass


