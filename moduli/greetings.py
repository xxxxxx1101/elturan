
# def  greet (name,age):
#     print(f'имя{name,}возраст{age}')


# from greetings import greet

# greet("Sardor",45)
# greet("nux",34)
# greet('Any',22)






# import pygame
# import time
# import random

# # Инициализация Pygame
# pygame.init()

# # Определение цветов
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # Размеры окна игры
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Змейка")

# # Функция для отображения сообщения на экране
# def message(msg, color):
#     font_style = pygame.font.SysFont(None, 30)
#     rendered_msg = font_style.render(msg, True, color)
#     screen.blit(rendered_msg, [width/6, height/3])

# # Основная функция игры
# def gameLoop():
#     game_over = False
#     game_exit = False

#     # Начальные координаты и скорость змейки
#     x = width / 2
#     y = height / 2
#     snake_size = 10
#     x_change = 0
#     y_change = 0

#     # Координаты и размеры фрукта (еды)
#     food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
#     food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
#     food_size = 10

#     clock = pygame.time.Clock()

#     # Главный игровой цикл
#     while not game_exit:
#         while game_over:
#             screen.fill(BLACK)
#             message("Игра окончена! Нажмите C для продолжения или Q для выхода.", RED)
#             pygame.display.update()

#             # Обработка событий клавиатуры в режиме окончания игры
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     game_exit = True
#                     game_over = False
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_exit = True
#                         game_over = False
#                     if event.key == pygame.K_c:
#                         gameLoop()

#         # Обработка событий клавиатуры
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_exit = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x_change = -snake_size
#                     y_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x_change = snake_size
#                     y_change = 0
#                 elif event.key == pygame.K_UP:
#                     y_change = -snake_size
#                     x_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y_change = snake_size
#                     x_change = 0

#         # Обновление координат змейки
#         x += x_change
#         y += y_change

#         # Проверка на выход за границы окна
#         if x >= width or x < 0 or y >= height or y < 0:
#             game_over 