import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/push.png')
        self.rect = self.image.get_rect()  # картинка пушки
        self.screen_rect = screen.get_rect()  # изображение экрана
        self.rect.centerx = self.screen_rect.centerx  # центр пушки и центр экрана
        self.center = float(self.rect.centerx)  # преобразовали в число с точкой для плавности движения
        self.rect.bottom = self.screen_rect.bottom  # низ пушки
        self.mright = False  # move_right
        self.mleft = False  # move_left

    def output(self):  # отрисовать пушку
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1  # движение на + 1 вправо пока правый край пушки меньше правого края экрана
        if self.mleft and self.rect.left > 0:
            self.center -= 1  # пока левый край пушки больше о

        self.rect.centerx = self.center

    def create_gun(self):
        """размещает пушку по центру внизу"""
        self.center = self.screen_rect.centerx
