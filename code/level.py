import pygame

from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        #TO GET DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()

        #for sprite grup setp
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        #setup sprite
        self.create_map()
  
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row): #to give num for x,y pos
                x = col_index * TITLESIZE
                y = row_index * TITLESIZE
                if col == 'x': 
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                   self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)


    def run(self):
        #for updating and drawing
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        

class YSortCameraGroup(pygame.sprite.Group):
	def _init_(self):

		# general setup 
		super()._init_()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)