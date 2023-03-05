class Hearvibore(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 spead: int = 5, health: int = 20):
        super().__init__(coordinates, spead, health)
        self.health = health
        self.spead = spead

    def make_move(self, digit: int, map: Map):
        super().make_move(digit, map)
        field = map
        if 9 <= digit <= 16:  # Диапазон соседних клеток для атаки
            select_position = Selection(self.coordinates)  # Выбираем клетку для взаимодействия
            attack_sprite: tuple = select_position.interact(digit)  # Выбираем соседнюю клетку для атаки
            target_entity = field.check_spot_not_empty(*attack_sprite)  # Проверяем что клетка не пустая
            if target_entity is not None and isinstance(target_entity, Grass):  # Если на клетке травоядное атакуем
                field.meeting(self, target_entity)


