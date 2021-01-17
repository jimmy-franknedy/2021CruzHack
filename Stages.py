import pygame, sys
from pygame import mixer
import math
import random
import End_Screen


# Intialize the pygame
pygame.init()
pygame.mixer.init()

Powerup=pygame.mixer.Sound("MarioPowerup.wav")
Gamestart=pygame.mixer.Sound("Game_Start.wav")

# For printing time 
white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)
clock_x = 800
clock_y = 200
clock_surface = pygame.display.set_mode((clock_x,clock_y))
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('TIME', True, green, blue)
textRect = text.get_rect()
textRect.center = (clock_x // 2, clock_y // 2)

# create time
clock = pygame.time.Clock()

# Background
forest = pygame.image.load('forest.png')
jbe = pygame.image.load('jbe.png')
dorm = pygame.image.load('dorm.png')
endtime = 34000 #120000

# Trash Images
blueMaskImg = pygame.image.load('blueMask.png')
tinWrapperImg = pygame.image.load('tinWrapper.png')
redLighterImg = pygame.image.load('redLighter.png')

yerba = pygame.image.load('yerba.png')
yerba = pygame.transform.scale(yerba, (64,54))
coffee = pygame.image.load('coffee.png')
scantron = pygame.image.load('scantron.png')


#Trash Positions
maskX = 500
maskY = 400
lighterX = 350
lighterY = 350
tinX = 130
tinY = 130
cX = 140
cY = 50
yX = 90
yY = 430
sX= 200
sY= 200

# Player Images And Stats
playerImg = pygame.image.load('sammy.png')
playerX = 370
playerY = 400
playerX_change = 0
playerY_change = 0

# Assign Player Position
def player(x,y, screen):
    screen.blit(playerImg, (x, y))

# Assign Trash Position
def trash(i,x,y,screen):
    screen.blit(i, (x, y))


####Counter Just Added
# Score Set-Up
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10

# Score Show 
def show_score(x, y, totalTrash, screen):
    score = font.render("Score : " + str(totalTrash) + "/6", True, (0, 0, 0))
    screen.blit(score, (x, y))

def fade(screen, width, height, color = (0,0,0)):
    fade = pygame.Surface((width, height))
    fade.fill(color)
    for alpha in range(0, 200):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5) #120

def isCollision(playerX, playerY, trashX, trashY, flag, totalTrash):
    distance = math.sqrt(math.pow(playerX - trashX, 2) + (math.pow(playerY - trashY, 2)))
    if (distance < 58) and (flag == 1):
        pygame.mixer.Sound.play(Powerup)
        return True
    else:
        return False
    
def playSammy(screen):
    pygame.mixer.Sound.play(Gamestart)
    run = True
    
    # Player stats
    playerX_change = 0
    playerY_change = 0
    playerX = 370
    playerY = 400

    #Trash Stats
    totalTrash = 0
    maskflag = 1
    tinflag = 1
    lighterflag = 1

    # Just Added!!
    yerbaflag = 1
    coffeeflag = 1
    scantronflag = 1
    
    while run:
        # Tranistion from startscreen to black
        if 3000 > pygame.time.get_ticks() > 2000:
            fade(screen, 800, 500)

        # Actual Game
        if pygame.time.get_ticks() > 4000:
            # Add background
            screen.blit(forest, (0, 0))

            # Add trash to background
            if (maskflag == 1):
                trash(blueMaskImg, maskX, maskY, screen)
            if (lighterflag == 1):
                trash(redLighterImg, lighterX, lighterY, screen)
            if (tinflag == 1):
                trash(tinWrapperImg, tinX, tinY, screen)
            if (coffeeflag == 1):
                trash(coffee, cX, cY, screen)
            if (yerbaflag == 1):
                trash(yerba, yX, yY, screen)
            if (scantronflag == 1):
                trash(scantron, sX, sY, screen)
 

            #Check for arrow key event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # if keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -5
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 5
                    if event.key == pygame.K_DOWN:
                        playerY_change = 5
                    if event.key == pygame.K_UP:
                        playerY_change = -5
                # This statement makes sure Sammy stops moving after you let go of the arrow keys
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                            or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        playerX_change = 0
                        playerY_change = 0
            # Update Sammy's position
            playerX += playerX_change
            playerY += playerY_change

            # BOUNDARIES So sammy doesn't fly off the screen
            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736
            if playerY <= 0:
                playerY = 0
            elif playerY >= 436:
                playerY = 436

            # Update Sammy's position again and Trash score!
            player(playerX,playerY, screen)
            show_score(textX, testY, totalTrash, screen)
            
            # Collision Updates, Trash Count, Timer
            if isCollision(playerX, playerY, maskX, maskY, maskflag, totalTrash):
                maskflag = -1
                totalTrash +=1
            if isCollision(playerX, playerY, lighterX, lighterY, lighterflag, totalTrash):
                lighterflag = -1
                totalTrash +=1
            if isCollision(playerX, playerY, tinX, tinY, tinflag, totalTrash):
                tinflag = -1
                totalTrash +=1
            # JUST Added
            if isCollision(playerX, playerY, cX, cY, coffeeflag, totalTrash):
                coffeeflag = -1
                totalTrash +=1
            if isCollision(playerX, playerY, sX, sY, scantronflag, totalTrash):
                scantronflag = -1
                totalTrash +=1
            if isCollision(playerX, playerY, yX, yY, yerbaflag, totalTrash):
                yerbaflag = -1
                totalTrash +=1

            print("totalTrash after running isCollision:", totalTrash)

            mins, secs = divmod(pygame.time.get_ticks()-4000, 60000) 
            secs = int(str(secs)[:-3])
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r")
            text = font.render(timer, True, green, blue)
            clock_surface.blit(text, textRect)
            
        # This ends the game after 2 mins/exits to next screen
        if pygame.time.get_ticks() > endtime:
            fade(screen,800, 500, (255,0,0))
            End_Screen.loserScreen(screen)
            state = End_Screen.loserInteraction(screen)
            return state
            break

        # All Trash Found :), ya win!
        if totalTrash == 6:
            pygame.time.delay(500)
            fade(screen,800, 500, (0,0,0))
            End_Screen.winnerScreen(screen)
            state = End_Screen.winnerInteraction(screen)
            return state
            break
            
        pygame.display.update()