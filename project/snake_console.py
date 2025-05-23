import pygame
import random
import sys

# Initialize Pygame and sound module (even though sound isn't used here, good habit)
pygame.init()
pygame.mixer.init()

# Set up the screen size
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game (BW Retro)")

# Define color values in RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load a basic font for displaying text
font = pygame.font.SysFont("Courier New", 28)

# Control how fast the game updates
clock = pygame.time.Clock()

# Size of each block that makes up the snake and food
block_size = 20

# Function to draw text on the screen
def draw_text(text, x, y):
    label = font.render(text, True, WHITE)
    screen.blit(label, (x, y))

# Function to draw the snake using a list of (x, y) positions
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, WHITE, [x, y, block_size, block_size])

# Function to show the menu and let player choose difficulty
def show_menu():
    while True:
        screen.fill(BLACK)
        draw_text("🐍 SNAKE GAME", 200, 100)
        draw_text("1. Play Easy", 220, 150)
        draw_text("2. Play Medium", 220, 190)
        draw_text("3. Play Hard", 220, 230)
        draw_text("Q. Quit", 220, 270)
        pygame.display.update()

        # Wait for player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Return the speed (lower is slower, higher is harder)
                if event.key == pygame.K_1:
                    return 10
                elif event.key == pygame.K_2:
                    return 15
                elif event.key == pygame.K_3:
                    return 20
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Main game loop function
def game_loop(speed):
    # Initial position of the snake's head
    x, y = width // 2, height // 2

    # Initial movement direction
    x_change, y_change = 0, 0

    # Snake is a list of blocks (each block is [x, y])
    snake = []
    snake_len = 1

    # Generate initial food position
    food_x = random.randint(0, (width - block_size) // block_size) * block_size
    food_y = random.randint(0, (height - block_size) // block_size) * block_size

    running = True
    while running:
        screen.fill(BLACK)

        # Handle keyboard and quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                # Change snake direction with arrow keys
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

        # Move the snake's head
        x += x_change
        y += y_change

        # Check for collision with the wall
        if x < 0 or x >= width or y < 0 or y >= height:
            break  # End the game

        # Draw the food on screen
        pygame.draw.rect(screen, WHITE, [food_x, food_y, block_size, block_size])

        # Add new head position to snake list
        snake.append([x, y])

        # Remove tail if snake didn't just grow
        if len(snake) > snake_len:
            del snake[0]

        # Check for self-collision
        for segment in snake[:-1]:
            if segment == [x, y]:
                running = False  # End the game if head touches body

        # Draw the snake on screen
        draw_snake(snake)

        # Update the screen
        pygame.display.update()

        # Check if the snake ate the food
        if x == food_x and y == food_y:
            snake_len += 1  # Make snake longer
            # Generate new food
            food_x = random.randint(0, (width - block_size) // block_size) * block_size
            food_y = random.randint(0, (height - block_size) // block_size) * block_size

        # Control the game speed
        clock.tick(speed)

    # Show game over screen
    screen.fill(BLACK)
    draw_text("GAME OVER - Press C to Continue or Q to Quit", 40, height // 2 - 20)
    pygame.display.update()
    wait_for_restart(speed)

# Wait for player to restart or quit
def wait_for_restart(speed):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_c:
                    game_loop(speed)  # Restart the game

# Entry point of the program
if __name__ == "__main__":
    speed = show_menu()   # Show the menu and get difficulty speed
    game_loop(speed)      # Start the game
