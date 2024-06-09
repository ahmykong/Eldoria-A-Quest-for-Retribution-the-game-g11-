import pygame
import sys

pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MiniIt')

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

if __name__ == "__main__":
    start_screen()