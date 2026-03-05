import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("My First Game Screen")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 150, 255))

    pygame.display.update()

pygame.quit()
sys.exit()