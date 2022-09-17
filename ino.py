import pygame


class Ino(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()  # сделали прямоугольник из картинки инопланетяшки
        self.rect.x = self.rect.width  # отслеживаем ширину
        self.rect.y = self.rect.height  # отслеживаем высоту
        self.x = float(self.rect.x)  # отслеживаем положение Ино по горизонтали
        self.y = float(self.rect.y)  # отслеживаем положение Ино по вертикали

    def draw(self):
        """выводит пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещает пришельцев"""
        self.y += 0.1
        self.rect.y = self.y
