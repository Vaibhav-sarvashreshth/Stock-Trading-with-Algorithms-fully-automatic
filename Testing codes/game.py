import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# ---------------------- Constants & Configuration ---------------------- #
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
RED       = (255, 0, 0)
GREEN     = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY  = (40, 40, 40)

# Directions
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

# Fonts
FONT_SMALL = pygame.font.SysFont("comicsansms", 25)
FONT_MED   = pygame.font.SysFont("comicsansms", 40)
FONT_LARGE = pygame.font.SysFont("comicsansms", 50)

# ----------------------------- Game Classes ----------------------------- #
class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, new_direction):
        # Prevent the snake from reversing
        if (new_direction[0] * -1, new_direction[1] * -1) == self.direction:
            return
        self.direction = new_direction

    def move(self):
        current = self.get_head_position()
        x_dir, y_dir = self.direction
        new = ((current[0] + (x_dir * GRID_SIZE)) % WINDOW_WIDTH,
               (current[1] + (y_dir * GRID_SIZE)) % WINDOW_HEIGHT)
        # If the snake runs into itself, reset the game
        if new in self.positions[2:]:
            self.reset()
            return False
        else:
            self.positions.insert(0, new)
            self.positions.pop()
            return True

    def grow(self):
        # When eating food, add a segment (duplicate tail)
        tail = self.positions[-1]
        self.positions.append(tail)

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, DARKGRAY, rect, 1)

class Food:
    def __init__(self):
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, DARKGRAY, rect, 1)

# --------------------------- Utility Functions -------------------------- #
def draw_grid(surface):
    """Draws a grid on the background for a neat UI."""
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(surface, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(surface, DARKGRAY, (0, y), (WINDOW_WIDTH, y))

def draw_text_centered(surface, text, font, color, y_offset=0):
    """Helper to draw centered text on the screen."""
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + y_offset))
    surface.blit(text_surface, rect)

def show_start_screen(screen):
    """Displays the start screen until the player presses a key."""
    screen.fill(BLACK)
    draw_text_centered(screen, "Snake Game", FONT_LARGE, WHITE, -50)
    draw_text_centered(screen, "Press any key to start", FONT_MED, WHITE, 30)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def show_game_over(screen, score):
    """Displays a game over screen with the current score."""
    screen.fill(BLACK)
    draw_text_centered(screen, "Game Over", FONT_LARGE, RED, -50)
    draw_text_centered(screen, f"Score: {score}", FONT_MED, WHITE, 0)
    draw_text_centered(screen, "Press any key to play again", FONT_SMALL, WHITE, 50)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# ------------------------------- Main Loop ------------------------------ #
def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    score = 0

    show_start_screen(screen)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Allow both arrow keys and WASD for movement
                if event.key in [pygame.K_UP, pygame.K_w]:
                    snake.turn(UP)
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    snake.turn(DOWN)
                elif event.key in [pygame.K_LEFT, pygame.K_a]:
                    snake.turn(LEFT)
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    snake.turn(RIGHT)

        # Move the snake and check for self-collision
        alive = snake.move()
        if not alive:
            show_game_over(screen, score)
            snake.reset()
            score = 0
            food.randomize_position()

        # Check if the snake has eaten the food
        if snake.get_head_position() == food.position:
            snake.grow()
            score += 1
            food.randomize_position()

        # Draw everything
        screen.fill(BLACK)
        draw_grid(screen)
        snake.draw(screen)
        food.draw(screen)

        # Draw score
        score_surface = FONT_SMALL.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (5, 5))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
