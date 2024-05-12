import pygame

from settings import *
from tile import Tile
from player import Player

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
            for col_index, col in enumerate(row):#to give num for x,y pos
                x = col_index * TITLESIZE
                y = row_index * TITLESIZE
                if col == 'x': 
                    Tile((x,y),[self.visible_sprites])


    def run(self):
        #for updating and drawing
        self.visible_sprites.draw(self.display_surface)
