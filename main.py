import pygame
import random
import math

#pygame initialization
pygame.init()

#setting up the screen
screen = pygame.display.set_mode((800,600))

background = pygame.image.load('./background.png')

pygame.display.set_caption("space invaders")
icon = pygame.image.load('./ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('./space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemy = 6

for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load('./alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(40,150))
    enemyX_change.append(3)
    enemyY_change.append(40)

bulletImg = pygame.image.load('./bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0

def enemy(a,b,i):
    screen.blit(enemyImg[i],(a,b))

def player(x,y):
    screen.blit(playerImg ,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16,y + 10))

def iscollision(enemyX , enemyY , bulletX , bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#game loop 
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("left key is pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                # print("right key is pressed")
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("keystroke is released")
                playerX_change = 0
    
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    for i in range(no_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        collision = iscollision(enemyX[i], enemyY[i] , bulletX , bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(40,150)
            print(score)

        enemy(enemyX[i],enemyY[i] , i )

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    
    
    player(playerX,playerY)
    
    pygame.display.update()