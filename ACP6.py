import pygame
import random

pygame.init()
pygame.mixer.init()

# Screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level Up Game")

# Load Background Image
background = pygame.image.load("images (1).jpg")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))



# Score
score = 0
font = pygame.font.Font(None, 36)

# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT//2)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5


# Enemy Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-30)
        self.rect.y = random.randint(0, HEIGHT-30)


# Groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Create 7 enemies
for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Collision
    hits = pygame.sprite.spritecollide(player, enemy_group, False)
    if hits:
        score += 1
        collision_sound.play()

    # Draw background
    screen.blit(background,(0,0))

    # Draw sprites
    all_sprites.draw(screen)

    # Score text
    score_text = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()