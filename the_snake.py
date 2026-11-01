from random import choice, randint

import pygame

# Инициализация Pygame должна быть до создания экрана
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480  # Ширина и высота в пикселях
GRID_SIZE = 20  # Размер одной клетки в пикселях
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE  # Сколько всего клеток по горизонтали
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  # Сколько всего клеток по вертикали

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self):
        """Инициализирует базовые атрибуты объекта."""
        # Центральная точка экрана
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self):
        """Абстрактный метод для отрисовки (переопределяется)."""
        pass


class Apple(GameObject):
    """Дочерний класс для яблока."""

    def __init__(self):
        """Задает цвет и начальную позицию яблока."""
        super().__init__()
        self.body_color = APPLE_COLOR
        # Скобки, чтобы вызвать метод, а не просто сослаться на него
        self.randomize_position()

    def randomize_position(self):
        """Устанавливает случайное положение яблока на игровом поле."""
        # Берем рандомную клетку по горизонтали и переводим в пиксели
        x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
        # То же самое, только по вертикали
        y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        # Передаем кортеж со сгенерированными координатами
        self.position = (x, y)

    def draw(self):
        """Отрисовывает яблоко на игровой поверхности."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Дочерний класс для змейки."""

    def __init__(self):
        """Инициализирует начальное состояние змейки."""
        super().__init__()
        self.length = 1  # длина змейки
        # Список, содержащий позиции всех сегментов тела змейки
        self.positions = [self.position]
        self.direction = RIGHT  # по умолчанию движется вправо
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        # Изначально нет последнего сегмента для затирания
        self.last = None

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновляет позицию змейки, добавляя новую голову."""
        head = self.get_head_position()

        # Вычисляем новую координату X после движения
        # Умножаем направление на размер клетки для перемещения
        # Используем %, чтобы змея телепортировалась, а не врезалась в стену
        new_x = (head[0] + (self.direction[0] * GRID_SIZE)) % SCREEN_WIDTH
        # Вычисляем новую координату Y аналогично
        new_y = (head[1] + (self.direction[1] * GRID_SIZE)) % SCREEN_HEIGHT
        new_head = (new_x, new_y)

        # Добавляем новую координату головы вперед
        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            # Если не съела яблоко, удаляем последний сегмент
            self.last = self.positions.pop()
        else:
            # Если съела, ничего не удаляем, чтобы длина увеличилась
            self.last = None

    def draw(self):
        """Отрисовывает змейку на экране, затирая след."""
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [self.position]  # создаем список для координат
        # Выбираем случайное направление для движения
        self.direction = choice((UP, LEFT, RIGHT, DOWN))
        self.last = None


def handle_keys(game_object):
    """Обрабатывает нажатия клавиш для изменения направления."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основной игровой цикл."""
    apple = Apple()
    snake = Snake()

    while True:
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        # Если голова совпадает с яблоком, длина увеличивается
        if snake.get_head_position() == apple.position:
            snake.length += 1
            # Чтобы яблоко оказалось в новом месте
            apple.randomize_position()

            # Если голова совпадает с телом, сбрасываем (исключая саму голову)
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            # Очистка экрана от старой мертвой змейки
            screen.fill(BOARD_BACKGROUND_COLOR)

        apple.draw()
        snake.draw()

        pygame.display.update()
        clock.tick(SPEED)


if __name__ == '__main__':
    main()

