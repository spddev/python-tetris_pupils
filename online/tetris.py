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
прямоугольная сетка для фигур игры размером 10 x 20, таких как:
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
        self.color = shape_colors[shape.index(shape)]
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
    # список координат-позиций на игровой сетке
    positions = []
    # преобразование в формат фигуры
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        '..0..'
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
            # если её координата y больше, чем -1
            if pos[1] > -1:
                return False
    return True


# функция проверки условия проигрыша в игре
def check_lost(positions):
    pass


# функция получения фигуры
def get_shape():
    # возвращаем случайную фигуру из списка возможных
    return Piece(5, 0, random.choice(shapes))


# функция отрисовки текста посередине
def draw_text_middle(text, size, color, surface):
    pass


# функция отрисовки сетки игрового поля
def draw_grid(surface, grid):
    # Начальная координата x
    sx = TOP_LEFT_X
    # Начальная координата y
    sy = TOP_LEFT_Y
    # На экране рисуем сетку в виде серых линий
    for i in range(len(grid)):
        # Рисуем горизонтальные линии
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * BLOCK_SIZE), (sx + PLAY_WIDTH, sy + i * BLOCK_SIZE))
        for j in range(len(grid)):
            # Рисуем вертикальные линии
            pygame.draw.line(surface, (128, 128, 128), (sx + j * BLOCK_SIZE, sy),
                             (sx + j * BLOCK_SIZE, sy + PLAY_HEIGHT))


# функция очистки игровой сетки
def clear_rows(grid, locked):
    pass


# функция отрисовки следующей игровой фигуры
def draw_next_shape(shape, surface):
    pass


# функция отрисовки окна игрового поля
def draw_window(surface, grid):
    # заполняем экран игры чёрным цветом
    surface.fill((0, 0, 0))

    # инициализация шрифтов в pygame
    pygame.font.init()
    # устанавливаем нужный шрифт
    font = pygame.font.SysFont('comicsans', 60)
    # отображаем название игры на экране белым цветом
    label = font.render('ТЕТРИС', 1, (255, 255, 255))

    # показываем название игры в центре экрана
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
    # словарь "занятых" (заблокированных) позиций сетки игрового поля
    locked_positions = {}
    # создание сетки из словар "занятых" позиций сетки игрового поля
    grid = create_grid(locked_positions)

    # изменение фигуры
    change_piece = False
    # состояние запуска игры
    run = True
    # текущая фигура
    current_piece = get_shape()
    # cледующая фигура
    next_piece = get_shape()
    # внутриигровое время
    сlock = pygame.time.Clock()
    # время падения фигуры
    fall_time = 0
    # скорость падения фигуры
    fall_speed = 0.60
    # время увеличения скорости падения фигур на конкретном уровне
    level_time = 0

    # оcновной игровой цикл
    while run:
        # создаём сетку из "занятых" позиций
        grid = create_grid(locked_positions)
        # высчитываем время падения, исходя из разницы времён
        # между предыдущей итерацией цикла и текущей
        fall_time += сlock.get_rawtime()
        # высчитываем время падения фигур на конкретном уровне
        level_time += сlock.get_rawtime()
        сlock.tick()

        # если время падения фигуры на уровне больше 5 секунд
        if level_time / 1000 > 5:
            level_time = 0
        # если скорость падения фигуры больше, чем 0.12
        if fall_speed > 0.12:
            # то мы уменьшаем её на 0.007
            fall_speed -= 0.007
        # если время падения фигуры / 1000 больше, чем скорость падения
        if fall_time / 1000 > fall_speed:
            #  то мы обнуляем время падения
            fall_time = 0
            # уменьшаем координату y текущей фигуры на 1
            current_piece.y -= 1
            # если пространства сетки игрового поля не хватает, и координата y текущей фигуры больше 0
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
            # если зарегистрировано событие нажатия клавиш на клавиатуре
            if event.type == pygame.KEYDOWN:
                # если нажата клавиша "стрелка влево"
                if event.key == pygame.K_LEFT:
                    # уменьшаем на 1  координату x текущей фигуры
                    current_piece.x -= 1
                    # если пространства достаточно
                    if not(valid_space(current_piece, grid)):
                        # увеличиваем координату x текущей фигуры на 1
                        current_piece.x += 1
                # если нажата клавиша "стрелка вправо"
                if event.key == pygame.K_RIGHT:
                    # увеличиваем на 1 координату x текущей фигуры
                    current_piece += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece -= 1
                # если нажата клавиша "стрелка вниз"
                if event.key == pygame.K_DOWN:
                    # увеличиваем на 1 координату y текущей фигуры
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                # если нажата клавиша "стрелка вверх"
                if event.key == pygame.K_UP:
                    # вращаем фигуру
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

        # вызов функции отрисовки основного окна игры
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