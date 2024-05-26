import pygame
from debug import debug
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        #stats for the player
        self.stats = {'health': 100,'energy':60,'attack': 10,'magic': 4,'speed': 5}
        self.health = self.stats['health'] * 0.5
        self.exp = 123
        self.speed = self.stats['speed']


        self .direction = pygame.math.Vector2()  #direction for the player to walk
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites 

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

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox): #to tell a collison between horizonttal sprites
                    if self.direction.x > 0 : #moving right
                        self.hitbox.right = sprite.hitbox.left 
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox): #to tell a collison between horizonttal sprites
                    if self.direction.y > 0 : #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: 
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        #update and draw again
        self.input()
        self.move(self.speed)
        
        