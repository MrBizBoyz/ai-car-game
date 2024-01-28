import pygame, random
from constants import *

class Line2(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 30
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)





    def update(self):
        self.rect.y += self.speed
        if self.rect.top > GAME_HEIGHT:
            self.rect.bottom = 0
