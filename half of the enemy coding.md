import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self,goblin_dagger,pos,groups):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(goblin_dagger)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)

    def import_graphics(self,name)
        self.animations = {'idle':[],'move':[],'attack':[]}
        main = f'../graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
