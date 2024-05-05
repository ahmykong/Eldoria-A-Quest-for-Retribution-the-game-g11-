import pygame

from settings import *

class Level:
    def __init__(self):

        #TO GET DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()

        #for sprite grup setp
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        #setup sprite
        self.create_map()
  
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            print(row_index)
            print(row)

    def run(self):
        #for update and drawing the game
        pass