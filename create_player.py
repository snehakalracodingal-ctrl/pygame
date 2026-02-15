import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a rocket image based on the provided design
def create_rocket():
    surface = pygame.Surface((64, 64), pygame.SRCALPHA)
    
    # Draw rocket body (white)
    pygame.draw.rect(surface, (255, 255, 255), (20, 15, 24, 35))
    pygame.draw.rect(surface, (200, 200, 200), (20, 15, 24, 35), 1)
    
    # Draw nose cone (red)
    points = [
        (32, 5),   # Top point
        (20, 15),  # Bottom left
        (44, 15)   # Bottom right
    ]
    pygame.draw.polygon(surface, (255, 0, 0), points)
    pygame.draw.polygon(surface, (200, 0, 0), points, 2)
    
    # Draw window (red circle)
    pygame.draw.circle(surface, (255, 0, 0), (32, 25), 6)
    pygame.draw.circle(surface, (200, 0, 0), (32, 25), 6, 1)
    pygame.draw.circle(surface, (150, 150, 255), (32, 25), 3)
    
    # Draw fins (dark blue)
    # Left fin
    fin_points_left = [
        (20, 35),   # Top left of body
        (10, 50),   # Bottom left tip
        (20, 45)    # Bottom left of body
    ]
    pygame.draw.polygon(surface, (0, 0, 139), fin_points_left)
    pygame.draw.polygon(surface, (0, 0, 100), fin_points_left, 1)
    
    # Right fin
    fin_points_right = [
        (44, 35),   # Top right of body
        (54, 50),   # Bottom right tip
        (44, 45)    # Bottom right of body
    ]
    pygame.draw.polygon(surface, (0, 0, 139), fin_points_right)
    pygame.draw.polygon(surface, (0, 0, 100), fin_points_right, 1)
    
    # Draw flames
    # Orange flame
    flame_points_orange = [
        (25, 50),   # Left bottom of body
        (32, 60),   # Bottom tip
        (39, 50)    # Right bottom of body
    ]
    pygame.draw.polygon(surface, (255, 165, 0), flame_points_orange)
    
    # Yellow flame (inner)
    flame_points_yellow = [
        (28, 50),   # Left inner
        (32, 58),   # Bottom inner tip
        (36, 50)    # Right inner
    ]
    pygame.draw.polygon(surface, (255, 255, 0), flame_points_yellow)
    
    return surface

# Create the rocket image
print("Creating rocket player image...")
rocket = create_rocket()
pygame.image.save(rocket, 'player.png')
print("Created: player.png")

pygame.quit()
