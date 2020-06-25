import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()   # инициализирует настройки, необходимые Pygame для нормальной работы.
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # создает область, где прорисовываются лементы игры.
    pygame.display.set_caption("Alien Invasion")

    # Назначение цвета фона.
    bg_color = (230, 230, 230)

    # Создание корабля.
    ship = Ship(screen)

    # Запуск основного цикла игры.
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()

