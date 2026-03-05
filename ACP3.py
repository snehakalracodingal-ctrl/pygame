import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add Sprites")
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

x = 100
y = 100

x2 = 400
y2 = 200

speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill(white)

    pygame.draw.rect(screen, blue, (x, y, 50, 50))

    pygame.draw.rect(screen, red, (x2, y2, 50, 50))

    pygame.display.update()

pygame.quit()
sys.exit()