import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake block size and speed
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake function
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Main function
def main():
    clock = pygame.time.Clock()

    # Snake initial position and direction
    snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    dx, dy = BLOCK_SIZE, 0

    # Food initial position
    food_x, food_y = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        # Update snake position
        new_head = (snake[0][0] + dx, snake[0][1] + dy)
        snake.insert(0, new_head)

        # Check collision with the food
        if new_head[0] == food_x and new_head[1] == food_y:
            food_x, food_y = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        else:
            snake.pop()

        # Draw everything on the screen
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
        draw_snake(snake)

        # Check collision with the boundaries
        if (snake[0][0] < 0 or snake[0][0] >= SCREEN_WIDTH or
            snake[0][1] < 0 or snake[0][1] >= SCREEN_HEIGHT):
            pygame.quit()
            return

        pygame.display.update()
        clock.tick(SNAKE_SPEED)

if __name__ == "__main__":
    main()
