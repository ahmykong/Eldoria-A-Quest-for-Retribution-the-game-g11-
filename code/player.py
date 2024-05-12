import pygame
from debug import debug
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self .direction = pygame.math.Vector2()  #direction for the player to walk
        self.speed = 5 

    def input(self):
        keys = pygame.key.get_pressed()  #keyboard input

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y= 0 #to stop the player from moving in one direction

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x= 0 

    def move(self,speed):
        if self.direction.magnitude() != 0: #to reduce the speed if the player goees sideway
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * speed

    def update(self):
        #update and draw again
        self.input()
        self.move(self.speed)
        
        