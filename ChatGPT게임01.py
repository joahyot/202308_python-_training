import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaker Game")

# Player paddle
player_width = 100
player_height = 10
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

# Ball
ball_size = 20
ball_x = SCREEN_WIDTH // 2
ball_y = player_y - ball_size
ball_speed_x = 3
ball_speed_y = -3

# Blocks
block_width = 60
block_height = 20
num_blocks = 5
blocks = [pygame.Rect(x, 50, block_width, block_height) for x in range(100, 700, block_width + 20)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with player paddle
    if ball_y >= player_y and ball_x >= player_x and ball_x <= player_x + player_width:
        ball_speed_y = -ball_speed_y

    # Ball collision with blocks
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)
            break

    # Clear the screen
    screen.fill(WHITE)

    # Draw player paddle
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_size // 2)

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    pygame.display.flip()

    # Game over
    if ball_y >= SCREEN_HEIGHT:
        running = False

# Quit pygame
pygame.quit()
