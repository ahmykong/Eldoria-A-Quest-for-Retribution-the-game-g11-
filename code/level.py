import pygame

class Level:
    def __init__(self):

        #TO GET DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()
        #for sprite grup setp
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        #for update and drawing the game
        pass