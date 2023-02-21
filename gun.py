import pygame

class Gun():

    def __init__(self, screen):
        """ Инициализация пушки """

        self.screen = screen
        self.image = pygame.image.load('images\gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

        # преобразование, т.к rect раюотает с целыми числами.
        # сделано для более плавного движения обьекта
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """ Прорисовка пушки """
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """ Обновление позиции пушки """
        if self.mright and self.rect.right < self.screen_rect.right: # проверка выхода за пределы поля
            self.center += 1.5
        if self.mleft and self.rect.left > 0: # проверка выхода за пределы поля
            self.center -= 1.5

        self.rect.centerx = self.center