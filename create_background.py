import pygame
import random

# Initialize Pygame
pygame.init()

def create_space_background():
    surface = pygame.Surface((800, 500))
    
    # Dark space background
    surface.fill((5, 5, 25))  # Very dark blue
    
    # Add many small stars
    for _ in range(150):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        size = random.choice([1, 1, 1, 2])  # Most stars are small, some are medium
        brightness = random.choice([150, 200, 255])
        pygame.draw.circle(surface, (brightness, brightness, brightness), (x, y), size)
    
    # Add some twinkling/bright stars
    for _ in range(20):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        # Draw a small cross pattern for bright stars
        pygame.draw.line(surface, (255, 255, 255), (x-2, y), (x+2, y), 1)
        pygame.draw.line(surface, (255, 255, 255), (x, y-2), (x, y+2), 1)
        pygame.draw.circle(surface, (255, 255, 255), (x, y), 1)
    
    # Add moon
    moon_x, moon_y = 650, 80
    moon_radius = 40
    
    # Moon surface (light gray with some texture)
    pygame.draw.circle(surface, (220, 220, 220), (moon_x, moon_y), moon_radius)
    
    # Moon craters
    pygame.draw.circle(surface, (180, 180, 180), (moon_x - 10, moon_y - 5), 8)
    pygame.draw.circle(surface, (180, 180, 180), (moon_x + 15, moon_y + 10), 5)
    pygame.draw.circle(surface, (180, 180, 180), (moon_x + 5, moon_y - 15), 6)
    pygame.draw.circle(surface, (180, 180, 180), (moon_x - 5, moon_y + 12), 4)
    
    # Add asteroids
    # Asteroid 1
    ast1_x, ast1_y = 150, 120
    pygame.draw.circle(surface, (100, 80, 60), (ast1_x, ast1_y), 15)
    pygame.draw.circle(surface, (80, 60, 40), (ast1_x - 5, ast1_y - 3), 3)
    pygame.draw.circle(surface, (80, 60, 40), (ast1_x + 4, ast1_y + 2), 2)
    pygame.draw.circle(surface, (80, 60, 40), (ast1_x + 2, ast1_y - 5), 2)
    
    # Asteroid 2
    ast2_x, ast2_y = 400, 80
    pygame.draw.circle(surface, (90, 70, 50), (ast2_x, ast2_y), 12)
    pygame.draw.circle(surface, (70, 50, 30), (ast2_x - 3, ast2_y + 2), 2)
    pygame.draw.circle(surface, (70, 50, 30), (ast2_x + 3, ast2_y - 2), 2)
    
    # Asteroid 3 (smaller)
    ast3_x, ast3_y = 550, 200
    pygame.draw.circle(surface, (110, 90, 70), (ast3_x, ast3_y), 8)
    pygame.draw.circle(surface, (90, 70, 50), (ast3_x - 2, ast3_y), 1)
    
    # Asteroid 4 (farther, smaller)
    ast4_x, ast4_y = 250, 300
    pygame.draw.circle(surface, (120, 100, 80), (ast4_x, ast4_y), 6)
    
    # Asteroid 5
    ast5_x, ast5_y = 700, 350
    pygame.draw.circle(surface, (95, 75, 55), (ast5_x, ast5_y), 10)
    pygame.draw.circle(surface, (75, 55, 35), (ast5_x + 2, ast5_y - 2), 2)
    
    # Add some distant small asteroids (just dots)
    for _ in range(8):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        pygame.draw.circle(surface, (60, 40, 20), (x, y), 2)
    
    return surface

# Create the enhanced space background
print("Creating enhanced space background with stars, asteroids, and moon...")
background = create_space_background()
pygame.image.save(background, 'space.png')
print("Updated: space.png with enhanced features")

pygame.quit()
