import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add Elements to My Screen")

white = (255, 255, 255)
blue = (0, 100, 255)
red = (255, 0, 0)


font = pygame.font.SysFont("Arial", 30)
text = font.render("Welcome to My Game Screen", True, red)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(blue)

    
    pygame.draw.rect(screen, white, (200, 150, 200, 100))


    screen.blit(text, (120, 50))

    pygame.display.update()

pygame.quit()
sys.exit()