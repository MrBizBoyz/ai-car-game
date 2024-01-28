import pygame, random
from constants import *

class Car(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT // 2
        self.width = width
        self.height = height
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)
        self.hit = False





    def update(self, car2):
        self.rect.x = GAME_WIDTH // 2 - BLOCK_SIZE
        for car in car2:
            if pygame.sprite.collide_rect(self, car):
                self.hit = True

        self.key_input()


    def key_input(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()

        if keys[pygame.K_RIGHT]:
            self.move_right()
    def move_left(self):
        self.rect.x = 0 + BLOCK_SIZE
    def move_right(self):
        self.rect.x = GAME_WIDTH  - BLOCK_SIZE * 2 - BLOCK_SIZE
