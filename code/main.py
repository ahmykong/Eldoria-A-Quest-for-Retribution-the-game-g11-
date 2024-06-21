import pygame, sys
from settings import *
from level import Level

SCREEN_WIDTH = 1280	
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Eldoria')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
FONT = pygame.font.Font(None, 74)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def start_screen():
    while True:
        SCREEN.fill(WHITE)
        draw_text('Eldoria', FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text('Press any key to start', FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Eldoria')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1: # upgrade menu
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR) #background water i meant around the area
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS) # i dont hink this is important cuz dosent show the clock

if __name__ == '__main__':
	start_screen()
	game = Game()
	game.run()