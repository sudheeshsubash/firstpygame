import pygame,random
from pygame import mixer

pygame.init()
mixer.init()

# mixer.music.load("mixkit-martial-arts-punch-2052.wav")
mixer.music.load("Sneaky-Snitch.mp3")
mixer.music.set_volume(1)
mixer.music.play()
crash = pygame.mixer.Sound("mixkit-martial-arts-punch-2052.wav")


# display
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("S-Game")

# background
background = pygame.image.load("background.png")

# text
score=0
text =f"score :{score}"

# enemy
enemyimg = pygame.image.load("enemy.png")

enemyX = random.randint(0,750)
enemyY = random.randint(0,550)
changeenemyX = 0
changeenemyY = 0

def enemy(x,y):
    screen.blit(enemyimg,(enemyX,enemyY))

# car
carimg = pygame.image.load("car.png")
carX = 0
carY = 520
carchangex = 0
carchangey = 0
def car(x,y):
    screen.blit(carimg,(x,y))

running = True
# main loop
while running:
    screen.fill((2,0,100))
    enemy(enemyX,enemyY)

    for even in pygame.event.get():
        
        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_RIGHT:
                carchangex = 1
            if even.key == pygame.K_LEFT:
                carchangex = -1
            if even.key == pygame.K_UP:
                carchangey = -1
            if even.key == pygame.K_DOWN:
                carchangey = 1
        if even.type == pygame.KEYUP:
            if even.key == pygame.K_RIGHT or even.key == pygame.K_LEFT:
                carchangex = 0
            if even.key == pygame.K_UP or even.key == pygame.K_DOWN:
                carchangey = 0
        if even.type == pygame.QUIT:
            running = False

    carX += carchangex
    carY += carchangey

    if carX < 0 or carX > 730:
        carchangex = 0
    if carY < 0 or carY > 530:
        carchangey = 0
    if (carX+32 > enemyX and enemyX +64 > carX+32)and(carY+32 > enemyY and enemyY +64 > carY+32):
        crash.play()
        enemyX = random.randint(0,750)
        enemyY = random.randint(0,550)
        enemy(enemyX,enemyY)
    car(carX,carY)

    pygame.display.update()