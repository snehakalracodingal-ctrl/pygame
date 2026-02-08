import pygame
import sys

# Initialize pygame
pygame.init()

# Create game screen
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites Game")

# Colors
WHITE = (100, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprite sizes
SPRITE_WIDTH, SPRITE_HEIGHT = 40, 40

# Sprite positions
sprite1_x, sprite1_y = 50, 50      # controllable sprite
sprite2_x, sprite2_y = 300, 200    # static sprite

# Movement speed
speed = 5

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls for sprite1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1_x -= speed
    if keys[pygame.K_RIGHT]:
        sprite1_x += speed
    if keys[pygame.K_UP]:
        sprite1_y -= speed
    if keys[pygame.K_DOWN]:
        sprite1_y += speed

    # Fill background
    screen.fill(WHITE)

    # Draw sprites
    pygame.draw.rect(screen, BLUE, (sprite1_x, sprite1_y, SPRITE_WIDTH, SPRITE_HEIGHT))
    pygame.draw.rect(screen, RED, (sprite2_x, sprite2_y, SPRITE_WIDTH, SPRITE_HEIGHT))

    # Update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
