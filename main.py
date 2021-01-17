import pygame, sys
import pygame.gfxdraw
import Start_Screen
pygame.init()

#color pallette
blue= [6, 114, 132]
bright_blue = [15, 170, 195]
purple = [101, 6, 81]
orange = [167, 80, 8]
bright_orange = [220, 125, 45]
yellow =[238, 198, 54]
cyan = [37, 193, 167]

#set-up screen
screen = pygame.display.set_mode((800, 500)) #dimensions in px
pygame.display.set_caption('Save the Slugs')
screen.fill(cyan)

#title
myfont = pygame.font.SysFont('segoescript', 80)
textsurface = myfont.render('Save the Slugs', True, blue)
screen.blit(textsurface,(82,40))
myfont = pygame.font.SysFont('segoescript', 80)
textsurface = myfont.render('Save the Slugs', True, yellow)
screen.blit(textsurface,(85,45))

Start_Screen.initalizeButtons(screen) #draws start screen buttons

pygame.display.update() #update screen when all mods are written

def fade(width, height, color): 
    fade = pygame.Surface((width, height))
    fade.fill(color)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

#while loop to keep the program running
while True:
    for event in pygame.event.get(): #allow the display to close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        Start_Screen.buttonInteractions(screen) #changes button colors on start screen
        #Start_Screen.buttonText(screen) #adds text to start screen
 
    pygame.display.update()
                
