import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('🐍 Snake Game in Python')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (213, 50, 80)
green = (0, 255, 0)
blue  = (50, 153, 213)

# Snake and food size
block_size = 20
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)

def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [width // 6, height // 3])

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, black, [block[0], block[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(blue)
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == [x, y]:
                game_close = True

        draw_snake(snake)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(10)  # Adjust speed here

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
