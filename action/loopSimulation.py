import msvcrt
from time import sleep

from action.PathFinding.finding_path import FindPath
from action.entity_actions import Action
from action.entity_spawn.entity_spawn import SpawnEntity
from instance_of_the_world.simulation_objects.dinamic_objects import Herbivore, Predator
from instance_of_the_world.simulation_objects.static_objects import Grass, Tree
from map.maps import Map
from render.render import RenderField


class LiveCycle:
    """
    Класс для запуска симуляции

        ...

    Attribute
    ---------
    self.map = map
        содержит текущую карту
    self.current_population = map.counting_population()
        содержит набор изначальный набор существ на карте
    self.continue_simulation
        содержит маркер выхода из бесконечной симуляции

    Methods
    -------
    endless_loop(self)
        Метод запускает бесконечную симуляцию на карте

    meaninglessness_of_being(self)
        метод для проверки что на карте есть травоядные и можно продолжать симуляцию.

    step_of_loop(self)
        метод для пошаговой отрисовки симуляции

    iteration_step(self)
        метод содержит цикл хода всех существ на карте
        
    __animal_step(self, hunter, pray)
        метод для выбора действия существа в зависимотри от местоположения цели
    """

    def __init__(self, map: Map):
        self.map = map
        self.current_population = map.counting_population(map)
        self.__stop_simulation = 'q'
        self.__step_by_step_simulation = 's'
        self.__return_in_endless_loop = 'r'
        self.continue_simulation = True
        print('Для остановки симуляции нажмите q',
              'Для перехода в пошаговую симуляцию s', sep='\n')

    def endless_loop(self) -> None:
        """
        Метод для запуска бесконечного цикла
        :return: None
        """
        RenderField().render(self.map)
        sleep(3)
        print('-------------------------')
        while not self.meaninglessness_of_being() or self.continue_simulation:
            if msvcrt.kbhit():
                __press_key = msvcrt.getwch()
                if __press_key == self.__stop_simulation:
                    self.continue_simulation = False
                    print('Принудительная остановка')
                    break

                elif __press_key == self.__step_by_step_simulation:
                    self.step_of_loop()

            self.iteration_step()

    def step_of_loop(self) -> None:
        """
        Метод для отрисовки одного хода
        :return:None
        """
        while True:
            print('Для выхода нажмите r после отрисовки')
            __custom_input: int = int(input('Какое число шагов нужно вывести?: '))
            if (__custom_input != self.__return_in_endless_loop
                    and isinstance(__custom_input, int)):
                while (__custom_input != 0
                       and not self.meaninglessness_of_being()):
                    self.iteration_step()
                    __custom_input -= 1
                    sleep(2)
            elif not isinstance(__custom_input, int):
                print('число шагов должнобыть целым числом')
            if msvcrt.kbhit():
                __user_press_key = msvcrt.getwch()
                if __user_press_key == self.__return_in_endless_loop:
                    print('Продолжаем симуляцию')
                    break

    def iteration_step(self) -> None:
        """
        Один шаг цикла
        :return: None
        """
        for entity in self.current_population:
            if isinstance(entity, Predator):
                self.__animal_step(entity, Herbivore)
            if isinstance(entity, Herbivore):
                self.__animal_step(entity, Grass)

    def __animal_step(self, hunter, pray) -> None:
        """
        Выбор действия существа
        :return: None
        """
        path = FindPath(hunter, pray, self.map).finding_path()
        Action(self.map).make_move(hunter, path)
        print('-------------------------')
        sleep(0.5)

    def meaninglessness_of_being(self) -> bool:
        """
        Проверяет остались ли на карте травоядные
        :return: bool
        """
        __herbivore_population = 0
        __grass_population = 0
        check_population: list = self.map.counting_population(self.map)
        for entity in check_population:
            if isinstance(entity, Herbivore):
                __herbivore_population += 1
            if isinstance(entity, Grass):
                __grass_population += 1

        if __herbivore_population == 0:
            self.continue_simulation = False
            print('Симуляция завершена')
            return True
        else:
            __grass_balance = __grass_population / __herbivore_population
            if __grass_balance < 3:
                for i in range(__herbivore_population):
                    each = Grass()
                    SpawnEntity(self.map).add_to_map(each, 1)
        return False
