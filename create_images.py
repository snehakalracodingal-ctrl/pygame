import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a simple space background
def create_background():
    surface = pygame.Surface((800, 500))
    surface.fill((0, 0, 20))  # Dark blue background
    
    # Add some stars
    for _ in range(100):
        x = pygame.time.get_ticks() % 800
        y = (pygame.time.get_ticks() * 7) % 500
        pygame.draw.circle(surface, (255, 255, 255), (x, y), 1)
    
    return surface

# Create a simple spaceship
def create_spaceship():
    surface = pygame.Surface((64, 64), pygame.SRCALPHA)
    
    # Draw spaceship body
    points = [
        (32, 10),   # Top point
        (10, 50),   # Bottom left
        (20, 45),   # Inner left
        (32, 35),   # Center bottom
        (44, 45),   # Inner right
        (58, 50)    # Bottom right
    ]
    pygame.draw.polygon(surface, (100, 200, 255), points)
    pygame.draw.polygon(surface, (150, 220, 255), points, 2)
    
    # Draw cockpit
    pygame.draw.circle(surface, (200, 200, 255), (32, 30), 8)
    
    return surface

# Create a simple enemy
def create_enemy():
    surface = pygame.Surface((64, 64), pygame.SRCALPHA)
    
    # Draw enemy body (octopus-like)
    pygame.draw.ellipse(surface, (255, 100, 100), (10, 20, 44, 30))
    pygame.draw.ellipse(surface, (255, 150, 150), (10, 20, 44, 30), 2)
    
    # Draw tentacles
    for i in range(6):
        x = 15 + i * 8
        pygame.draw.line(surface, (255, 100, 100), (x, 50), (x, 60), 3)
    
    # Draw eyes
    pygame.draw.circle(surface, (255, 255, 255), (25, 35), 4)
    pygame.draw.circle(surface, (255, 255, 255), (39, 35), 4)
    pygame.draw.circle(surface, (0, 0, 0), (25, 35), 2)
    pygame.draw.circle(surface, (0, 0, 0), (39, 35), 2)
    
    return surface

# Create a simple bullet
def create_bullet():
    surface = pygame.Surface((32, 32), pygame.SRCALPHA)
    
    # Draw bullet
    pygame.draw.ellipse(surface, (255, 255, 0), (12, 8, 8, 16))
    pygame.draw.ellipse(surface, (255, 200, 0), (12, 8, 8, 16), 2)
    
    return surface

# Create a UFO icon
def create_ufo():
    surface = pygame.Surface((64, 64), pygame.SRCALPHA)
    
    # Draw UFO body
    pygame.draw.ellipse(surface, (150, 150, 200), (10, 35, 44, 20))
    pygame.draw.ellipse(surface, (200, 200, 255), (10, 35, 44, 20), 2)
    
    # Draw dome
    pygame.draw.ellipse(surface, (100, 200, 255), (20, 20, 24, 20))
    pygame.draw.ellipse(surface, (150, 220, 255), (20, 20, 24, 20), 2)
    
    # Draw lights
    for i in range(5):
        x = 15 + i * 8
        pygame.draw.circle(surface, (255, 255, 0), (x, 45), 2)
    
    return surface

# Create all images
print("Creating PNG images...")

# Background
background = create_background()
pygame.image.save(background, 'space.png')
print("Created: space.png")

# Spaceship
spaceship = create_spaceship()
pygame.image.save(spaceship, 'spaceship.png')
print("Created: spaceship.png")

# Enemy
enemy = create_enemy()
pygame.image.save(enemy, 'enemy.png')
print("Created: enemy.png")

# Bullet
bullet = create_bullet()
pygame.image.save(bullet, 'bullet.png')
print("Created: bullet.png")

# UFO icon
ufo = create_ufo()
pygame.image.save(ufo, 'ufo.png')
print("Created: ufo.png")

print("All images created successfully!")
pygame.quit()
