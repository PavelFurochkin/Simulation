import msvcrt
import os
from time import sleep

from action import GrassSpawn
from action.actions import Action
from action.turn_actions.PathFinding.finding_path import FindPath
from instance_of_the_world import Grass
from instance_of_the_world import Herbivore, Predator
from map.maps import Map
from render.render import RenderField


class LiveCycle(Action):
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
        метод для проверки что на карте есть травоядные
         и можно продолжать симуляцию.

    step_of_loop(self)
        метод для пошаговой отрисовки симуляции

    iteration_step(self)
        метод содержит цикл хода всех существ на карте
        
    __animal_step(self, hunter, pray)
        метод для выбора действия существа в зависимотри от местоположения цели
    """
    def __init__(self, map: Map):
        super().__init__(map)

        self.current_population = map.counting_population()
        self.__stop_simulation = 'q'
        self.__step_by_step_simulation = 's'
        self.__return_in_endless_loop = 'r'
        self.continue_simulation = True
        print('Для остановки симуляции нажмите q',
              'Для перехода в пошаговую симуляцию s', sep='\n')

    def perform(self) -> None:
        """
        Метод для запуска бесконечного цикла
        :return: None
        """
        RenderField().render(self.map)
        sleep(3)
        os.system('cls')
        while self.meaninglessness_of_being() or self.continue_simulation:
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
            print('Для выхода нажмите r')
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
            if isinstance(entity, Herbivore) and entity.health > 0:
                self.__animal_step(entity, Grass)

    def __animal_step(self, hunter, pray) -> None:
        """
        Выбор действия существа
        :return: None
        """
        path = FindPath(hunter, pray, self.map).finding_path()
        RenderField().render(self.map)
        hunter.make_move(self.map, hunter, path)
        sleep(0.5)
        os.system('cls')

    def meaninglessness_of_being(self) -> bool:
        """
        Проверяет остались ли на карте травоядные
        :return: bool
        """
        __herbivore_population = 0
        __grass_population = 0
        check_population: list = self.map.counting_population()
        for entity in check_population:
            if isinstance(entity, Herbivore):
                __herbivore_population += 1
            if isinstance(entity, Grass):
                __grass_population += 1

        if __herbivore_population == 0:
            self.continue_simulation = False
            print('Симуляция завершена')
            return False
        if __grass_population < self.map.matrix_size() * 0.05:
            GrassSpawn(self.map).perform()
        return True
