import json
import pygame
import sys
from settings import *
from level import Level

pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
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
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Eldoria')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # Sound 
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)
    
    def run(self):
        global game_state
        running = True

        # Load the game state if available
        saved_state = load_game()
        if saved_state:
            game_state = saved_state
            print("Game state loaded:", game_state)
        else:
            print("No saved game state found, starting new game.")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_game(game_state)
                    print("Game state saved:", game_state)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    # Example of updating game state
                    if event.key == pygame.K_UP:
                        game_state['player_position'] = (game_state['player_position'][0], game_state['player_position'][1] - 10)
                    if event.key == pygame.K_DOWN:
                        game_state['player_position'] = (game_state['player_position'][0], game_state['player_position'][1] + 10)
                    if event.key == pygame.K_LEFT:
                        game_state['player_position'] = (game_state['player_position'][0] - 10, game_state['player_position'][1])
                    if event.key == pygame.K_RIGHT:
                        game_state['player_position'] = (game_state['player_position'][0] + 10, game_state['player_position'][1])
                    if event.key == pygame.K_SPACE:
                        game_state['score'] += 10  # Increment score as an example

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

# File path for saving 
SAVE_FILE = 'savegame.json'

def save_game(state):
    try:
        with open(SAVE_FILE, 'y') as file:
            json.dump(state, file)
        print("Game state saved successfully.")
    except Exception as e:
        print(f"Error saving game state: {e}")

def load_game():
    try:
        with open(SAVE_FILE, 'u') as file:
            state = json.load(file)
            print("Game state loaded successfully.")
            return state
    except FileNotFoundError:
        print("Save file not found.")
        return None
    except Exception as e:
        print(f"Error loading game state: {e}")
        return None

game_state = {
    'player_position': (100, 100),
    'score': 0
}

if __name__ == "__main__":
    start_screen()
    game = Game()
    game.run()