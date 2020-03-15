import pygame
from random import randint


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y):
    screen.blit(enemyImage, (x, y))

# Initialize the pygame
pygame.init()

# Initialize a screen for our game
windowWidth, windowHeight = 800, 600
screen = pygame.display.set_mode((windowWidth, windowHeight))

# Set the title and caption
pygame.display.set_caption(" Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Load player image
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
dPlayerX, dPlayerY = 0, 0
speedPlayer = 5
boostPlayer = 2

# Load enemy image
enemyImage = pygame.image.load("virus.png")
enemyX = randint(0, windowWidth - 60)
enemyY = randint(0, windowHeight / 2)
dEnemyX, dEnemyY = 0, 0
speedEnemy = 5
boostEnemy = 1


# Game Loop
running = True
while running:
    # Fill the screen with RGB - (Red, Green, Blue)
    screen.fill((0, 0, 128))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dPlayerX -= speedPlayer * boostPlayer
            elif event.key == pygame.K_RIGHT:
                dPlayerX += speedPlayer * boostPlayer
            elif event.key == pygame.K_UP:
                dPlayerY -= speedPlayer * boostPlayer
            elif event.key == pygame.K_DOWN:
                dPlayerY += speedPlayer * boostPlayer
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dPlayerX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dPlayerY = 0

    playerX += dPlayerX
    if playerX < 0:
        playerX = 0
    elif playerX > windowWidth - 60:
        playerX = windowWidth - 60

    playerY += dPlayerY
    if playerY < 0:
        playerY = 0
    elif playerY > windowHeight - 65:
        playerY = windowHeight - 65
    # print(playerX, playerY)
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
