import sys

import pygame

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()   # инициализирует настройки, необходимые Pygame для нормальной работы.
    screen = pygame.display.set_mode((1200, 800))   # создает отображаемую область, на которой прорисовываются все графические элементы игры. Аргумент (1200, 800) представляет собой кортеж, определяющий размеры игрового окна.
    pygame.display.set_caption("Alien Invasion")

    # Назначение цвета фона.
    bg_color = (230, 230, 230)

    # Запуск основного цикла игры.
    while True:     # цикл, который управляет обновлениями экрана.
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # При каждом проходе цикла перерисовывается экран.
            screen.fill(bg_color)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()