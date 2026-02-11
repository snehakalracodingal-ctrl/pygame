import math
import random
import pygame
import os

# ================== CONSTANTS ==================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# ================== INITIALIZE ==================
pygame.init()

# Base directory (IMPORTANT for Mac)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ================== LOAD IMAGES ==================
background = pygame.image.load(os.path.join(BASE_DIR, 'background.png'))
icon = pygame.image.load(os.path.join(BASE_DIR, 'ufo.png'))
playerImg = pygame.image.load(os.path.join(BASE_DIR, 'player.png'))
bulletImg = pygame.image.load(os.path.join(BASE_DIR, 'bullet.png'))

pygame.display.set_caption("Space Invader")
pygame.display.set_icon(icon)

# ================== PLAYER ==================
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# ================== ENEMY ==================
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _ in range(num_of_enemies):
    enemyImg.append(
        pygame.image.load(os.path.join(BASE_DIR, 'enemy.png'))
    )
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# ================== BULLET ==================
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"  # ready or fire

# ================== SCORE ==================
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)


# ================== FUNCTIONS ==================
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 +
                         (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE


# ================== GAME LOOP ==================
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    # Enemy Movement
    for i in range(num_of_enemies):

        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
