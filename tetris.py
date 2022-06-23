import pygame
import random

# создание структуры данных для игровых фигур
# установка глобальных переменных
# функции
# - построение "сетки"
# - отрисовка "сетки"
# - отрисовка окна
# - реализация поворота фигур в главной функции main
# - код главной функции main

"""
квадратная сетка для фигур игры размером 10 x 20, таких как:
S, Z, I, O, J, L, T,
представленных в порядке от 0 до 6 
"""

# инициализация шрифтов в библиотеке pygame
pygame.font.init()

# Глобальные переменные
S_WIDTH = 800
S_HEIGHT = 700
PLAY_WIDTH = 300  # означает: 300 // 10 = 30 - ширина на блок
PLAY_HEIGHT = 600  # означает: 600 // 20 = 30 - высота на блок
BLOCK_SIZE = 30  # размер блока

# x-координата левого верхнего угла
TOP_LEFT_X = (S_WIDTH - PLAY_WIDTH) // 2
# y-координата левого верхнего угла
TOP_LEFT_Y = S_HEIGHT - PLAY_HEIGHT

# Форматы фигур
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
# список основных фигур игры
shapes = [S, Z, I, O, J, L, T]
# список цветов основных фигур
# индекс 0 - 6 представляет конкретную фигуру
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


# класс параметров конкретной фигуры
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


# функция создание сетки для размещения фигур игры
def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


# функция преобразования формата фигуры
def convert_shape_format(shape):
    # список координат позиций на игровой сетке
    positions = []
    # преобразование в формат фигуры
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        # '..0..'
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions


# функция проверки правильного размещения фигуры на сетке игрового поля
def valid_space(shape, grid):
    # список всех возможных позиций сетки экрана
    # [[(0, 1)]], [[(2, 3)]] --> [[(0, 1), (2, 3)]]
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]
    # отформатированные позиции
    formatted = convert_shape_format(shape)

    # Цикл по всем отформатированным позициям
    for pos in formatted:
        # если позиция не содержится в списке возможных позиций
        if pos not in accepted_pos:
            # если координата y позиции больше, чем -1
            if pos[1] > -1:
                return False
    return True


# функция проверки условия проигрыша в игре
def check_lost(positions):
    pass


# функция получения фигуры
def get_shape():
    # возвращаем случайную фигуру из списка возможных фигур игры тетрис
    return Piece(5, 0, random.choice(shapes))


# функция отрисовки текста посередине
def draw_text_middle(text, size, color, surface):
    pass


# функция отрисовки сетки игрового поля
def draw_grid(surface, grid):
    pass


# функция очистки игровой сетки
def clear_rows(grid, locked):
    pass


# функция отрисовки следующей игровой фигуры
def draw_next_shape(shape, surface):
    pass


# функция отрисовки окна игрового поля
def draw_window(surface, grid):
    # заполняем игровую область чёрным цветом
    surface.fill((0, 0, 0))

    # инициализация шрифтов в игре
    pygame.font.init()
    # устанавливаем шрифт
    font = pygame.font.SysFont('comicsans', 60)
    # отображаем название игры на экране белым цветом
    label = font.render('ТЕТРИС', 1, (255, 255, 255))

    # отображаем название игры в центре экрана
    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (TOP_LEFT_X + j * BLOCK_SIZE,
                                                   TOP_LEFT_Y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    pygame.draw.rect(surface, (255, 0, 0), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 4)

    draw_grid(surface, grid)
    pygame.display.update()


# основная функция игры
def main(win):
    # словарь "занятых" позиций сетки
    locked_positions = {}
    # создание сетки из словаря "занятых" позиций
    grid = create_grid(locked_positions)

    # изменение фигуры
    change_piece = False
    # состояние запуска игры
    run = True
    # текущая фигура
    current_piece = get_shape()
    # следующая фигура
    next_piece = get_shape()
    # внутриигровое время
    clock = pygame.time.Clock()
    # время падения фигуры
    fall_time = 0
    # скорость падения фигуры
    fall_speed = 0.60
    # время увеличения скорости падения фигур на игровом уровне
    level_time = 0

    # основной игровой цикл
    while run:
        # создаём сетку из "занятых" позиций
        grid = create_grid(locked_positions)
        # рассчитываем время падения, исходя из разницы
        # между временем предыдущей итерации цикла и текущей
        fall_time += clock.get_rawtime()
        # рассчитываем время падения фигур на конкретном уровне
        level_time += clock.get_rawtime()
        clock.tick()

        # если время падения фигур на уровне больше 5 секунд
        if level_time / 1000 > 5:
            level_time = 0
        # если скорость падения фигуры больше, чем 0.12
        if fall_speed > 0.12:
            # уменьшаем скорость на 0.007
            fall_speed -= 0.007
        # если время падения фигуры / 1000 больше, чем скорость падения
        if fall_time / 1000 > fall_speed:
            # обнуляем время падения
            fall_time = 0
            # увеличиваем координату y текущей фигуры на 1
            current_piece.y += 1
            # если пространства сетки не хватает и координата y текущей фигуры больше 0
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                # уменьшаем координату y на 1
                current_piece.y -= 1
                # выставляем флаг смены фигуры в значение "истина"
                change_piece = True
        # анализ игровых событий
        for event in pygame.event.get():
            # если получено событие выхода из игры
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            # если получено событие нажатия клавиш
            if event.type == pygame.KEYDOWN:
                # если нажата клавиша "стрелка влево"
                if event.key == pygame.K_LEFT:
                    # уменьшаем координату x фигуры на 1
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                # если нажата клавиша "стрелка вправо"
                if event.key == pygame.K_RIGHT:
                    # увеличиваем координату x фигуры на 1
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1
                # если нажата клавиша "стрелка вверх"
                if event.key == pygame.K_UP:
                    # вращаем фигуру
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
                # если нажата клавиша "стрелка вниз"
                if event.key == pygame.K_DOWN:
                    # увеличиваем на 1 текущую координату y фигуры
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        # если фигура сменилась
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                # {(1, 2): (255, 0, 0)}
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        # вызов функции отображения основного окна игры
        draw_window(win, grid)
        pygame.display.update()


# функция отображения главного меню
def main_menu(win):
    main(win)


# задаём размеры окна нашей игры
win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
# указываем название игры в заголовке окна
pygame.display.set_caption('Тетрис')

main_menu(win)