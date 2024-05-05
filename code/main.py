import pygame, sys
from settings import *  
from level import Level

class Game:
    def __init__(self):

        #this fir generao setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Eldoria: A Quest for Retribution')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        #in the game alr
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
