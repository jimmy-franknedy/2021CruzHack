# End Screen Scenes
import pygame, sys
import pygame.gfxdraw
pygame.init()

pygame.mixer.init()

GameEndSound=pygame.mixer.Sound("Sadsound.wav")
Winnersound=pygame.mixer.Sound("HappyGameEnd_sound.wav")
#windowSize = (800, 500)
#screen = pygame.display.set_mode(windowSize)

#color pallette
blue = [6, 114, 132]
bright_blue = [15, 170, 195]
purple = [101, 6, 81]
orange = [167, 80, 8]
bright_orange = [220, 125, 45]
yellow = [238, 198, 54]
bright_yellow = [255, 230, 140]
cyan = [37, 193, 167]
white = [255, 255, 255]
gray = [176, 176, 176]
red = [255, 0, 0]


#################################
# function to draw rounded rect
def draw_rounded_rect(surface, rect, color, corner_radius):
    ''' Draw a rectangle with rounded corners.
    Would prefer this: 
        pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
    but this option is not yet supported in my version of pygame so do it ourselves.

    We use anti-aliased circles to make the corners smoother
    '''
    if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
        raise ValueError(
            f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})"
        )

    # need to use anti aliasing circle drawing routines to smooth the corners
    pygame.gfxdraw.aacircle(surface, rect.left + corner_radius,
                            rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1,
                            rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.left + corner_radius,
                            rect.bottom - corner_radius - 1, corner_radius,
                            color)
    pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1,
                            rect.bottom - corner_radius - 1, corner_radius,
                            color)

    pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius,
                                 rect.top + corner_radius, corner_radius,
                                 color)
    pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1,
                                 rect.top + corner_radius, corner_radius,
                                 color)
    pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius,
                                 rect.bottom - corner_radius - 1,
                                 corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1,
                                 rect.bottom - corner_radius - 1,
                                 corner_radius, color)

    rect_tmp = pygame.Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)


#########################################################


########################################
# LOSER SCREEN
#   will display a bruning forest when time runs out for player
#   will then give 3 choices on how to proceed with the program
########################################
def loserScreen(screen):
    pygame.mixer.Sound.play(GameEndSound) #Sound played when on loser screen
    
    background = pygame.image.load('forest_fire.jpg')
    screen.blit(screen, (0, 0))
    screen.blit(background, (0, 0))

    # end screen text
    myfont = pygame.font.SysFont('impact', 100)
    textsurface = myfont.render('OH NO!', True, (0,0,0))
    screen.blit(textsurface,(260,7))
    textsurface = myfont.render('OH NO!', True, yellow)
    screen.blit(textsurface,(265,10))
    
    myfont = pygame.font.SysFont('Comic Sans MS', 60)
    textsurface = myfont.render('You didn\'t save the slugs :(', True, (0,0,0))
    screen.blit(textsurface,(22,105))
    textsurface = myfont.render('You didn\'t save the slugs :(', True, yellow)
    screen.blit(textsurface,(25,108))
    
    #initalize buttons
    #Home Screen button
    home_button = pygame.Rect(110, 200, 250, 130)
    draw_rounded_rect(screen, home_button, blue, 15)
    home_shadow = pygame.Rect(100, 190, 270, 150)
    draw_rounded_rect(screen, home_shadow, cyan, 15)

    #Exit Button
    exit_button = pygame.Rect(440, 200, 250, 130)
    draw_rounded_rect(screen, exit_button, white, 15)
    exit_shadow = pygame.Rect(430, 190, 270, 150)
    draw_rounded_rect(screen, exit_shadow, gray, 15)
    pygame.display.update()


def loserInteraction(screen):
    end = True
    while end:
        for event in pygame.event.get():
            #if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()  #get coordinates of mouse
            # if x-pos + width > .... > x-pos and y-pos + height > ... >y-pos

            #home screen button
            if ((110 + 250) > mouse[0] > 110) and (
                (200 + 130) > mouse[1] > 200):
                home_button = pygame.Rect(110, 200, 250, 130)
                draw_rounded_rect(screen, home_button, bright_blue, 15)

                click = pygame.mouse.get_pressed()  #check on click
                if click[0]:  #if mouse is clicked on how to button
                    return "home"

            #exit button
            elif ((440 + 250) > mouse[0] > 440) and (
                (200 + 130) > mouse[1] > 220):
                exit_button = pygame.Rect(440, 200, 250, 130)
                draw_rounded_rect(screen, exit_button, white, 15)

                click = pygame.mouse.get_pressed()  #check on click

                if click[0]:  #if mouse is clicked on how to button
                    pygame.quit()  #exit game
                    sys.exit()

            else:
                #Home Screen button
                home_button = pygame.Rect(110, 200, 250, 130)
                draw_rounded_rect(screen, home_button, blue, 15)
                home_shadow = pygame.Rect(100, 190, 270, 150)
                draw_rounded_rect(screen, home_shadow, cyan, 15)
                #Exit Button
                exit_button = pygame.Rect(440, 200, 250, 130)
                draw_rounded_rect(screen, exit_button, white, 15)
                exit_shadow = pygame.Rect(430, 190, 270, 150)
                draw_rounded_rect(screen, exit_shadow, gray, 15)
                

            #button text
            #Start Screen button text
            myfont = pygame.font.SysFont('Comic Sans MS', 55)
            textsurface = myfont.render('Home', True, yellow)
            screen.blit(textsurface, (160, 198))
            myfont = pygame.font.SysFont('Comic Sans MS', 55)
            textsurface = myfont.render('Screen', True, yellow)
            screen.blit(textsurface, (142, 252))
            #exit button text
            myfont = pygame.font.SysFont('Comic Sans MS', 55)
            textsurface = myfont.render('EXIT', True, red)
            screen.blit(textsurface, (492, 220))

            pygame.display.update()


########################################
# WINNER SCREEN
#   will display a nice healthy environment
#   will then give 2 choices on how to proceed with the program
########################################


def winnerScreen(screen):
    pygame.mixer.Sound.play(Winnersound)

    background = pygame.image.load('fox.jpg')
    screen.blit(screen, (0, 0))
    screen.blit(background, (0, 0))

    # end screen text
    myfont = pygame.font.SysFont('Comic Sans MS', 60)
    textsurface = myfont.render('Thank you for', True, (220,162,9))
    screen.blit(textsurface,(197,0))
    textsurface = myfont.render('Thank you for', True, yellow)
    screen.blit(textsurface,(200,2))

    myfont = pygame.font.SysFont('Comic Sans MS', 60)
    textsurface = myfont.render("Saving Sammy's friends!", True, (220,162,9))
    screen.blit(textsurface,(48,102))
    textsurface = myfont.render("Saving Sammy's friends!", True, yellow)
    screen.blit(textsurface,(45,102))
    
    #initalize buttons
    #Home Screen button
    home_button = pygame.Rect(110, 200, 250, 130)
    draw_rounded_rect(screen, home_button, blue, 15)
    home_shadow = pygame.Rect(100, 190, 270, 150)
    draw_rounded_rect(screen, home_shadow, cyan, 15)
    
    #Exit Button
    exit_button = pygame.Rect(440, 200, 250, 130)
    draw_rounded_rect(screen, exit_button, white, 15)
    exit_shadow = pygame.Rect(430, 190, 270, 150)
    draw_rounded_rect(screen, exit_shadow, gray, 15)
    pygame.display.update()


def winnerInteraction(screen):
    end = True
    while end:
        for event in pygame.event.get():
            #if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()  #get coordinates of mouse
            # if x-pos + width > .... > x-pos and y-pos + height > ... >y-pos

            #home screen button
            if ((110 + 250) > mouse[0] > 110) and (
                (200 + 130) > mouse[1] > 200):
                home_button = pygame.Rect(110, 200, 250, 130)
                draw_rounded_rect(screen, home_button, bright_blue, 15)

                click = pygame.mouse.get_pressed()  #check on click
                if click[0]:  #if mouse is clicked on how to button
                    return "home"

            #exit button
            elif ((440 + 250) > mouse[0] > 440) and (
                (200 + 130) > mouse[1] > 220):
                exit_button = pygame.Rect(440, 200, 250, 130)
                draw_rounded_rect(screen, exit_button, white, 15)

                click = pygame.mouse.get_pressed()  #check on click

                if click[0]:  #if mouse is clicked on how to button
                    pygame.quit()  #exit game
                    sys.exit()

            else:
                #Home Screen button
                home_button = pygame.Rect(110, 200, 250, 130)
                draw_rounded_rect(screen, home_button, blue, 15)
                home_shadow = pygame.Rect(100, 190, 270, 150)
                draw_rounded_rect(screen, home_shadow, cyan, 15)
                #Exit Button
                exit_button = pygame.Rect(440, 200, 250, 130)
                draw_rounded_rect(screen, exit_button, white, 15)
                exit_shadow = pygame.Rect(430, 190, 270, 150)
                draw_rounded_rect(screen, exit_shadow, gray, 15)

            #button text
            #Start Screen button text
            myfont = pygame.font.SysFont('Comic Sans MS', 55)
            textsurface = myfont.render('Home', True, yellow)
            screen.blit(textsurface, (160, 198))
            myfont = pygame.font.SysFont('Comic Sans MS', 55)
            textsurface = myfont.render('Screen', True, yellow)
            screen.blit(textsurface, (142, 252))
            #exit button text
            myfont = pygame.font.SysFont('Comic Sans MS', 55)
            textsurface = myfont.render('EXIT', True, red)
            screen.blit(textsurface, (492, 220))

            pygame.display.update()


#loserScreen(screen)
#loserInteraction(screen)

#winnerScreen(screen)
#winnerInteraction(screen)