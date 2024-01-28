import pygame, random
from constants import *
import random

class Car2(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = 0 - BLOCK_SIZE
        self.width = width
        self.height = height
        self.speed = 5
        self.spawn = random.randint(0, 2)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0 ,0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)
        self.points = 0





    def update(self):

        self.loc()
        self.rect.y += self.speed
        if self.rect.top > GAME_WIDTH:
            self.rect.bottom = 0
            self.spawn = random.randint(0, 2)
            self.points += 1



    def loc(self):
        if self.spawn == 0:
            self.rect.x = 0 + BLOCK_SIZE
        if self.spawn == 1:
            self.rect.x = GAME_WIDTH // 2 - BLOCK_SIZE
        if self.spawn == 2:
            self.rect.x = GAME_WIDTH  - BLOCK_SIZE * 2 - BLOCK_SIZE
