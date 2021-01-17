# STS Start Screen
import pygame
import Stages 


#color pallette
baby_blue = [135 ,248, 255]
blue= [6, 114, 132]
bright_blue = [15, 170, 195]
purple = [101, 6, 81]
orange = [167, 80, 8]
baby_orange = [236, 107,0]
bright_orange = [190, 100, 0]
yellow =[238, 198, 54]
cyan = [37, 193, 167]

#images
slugImg = pygame.image.load('slug1.png')
slugImg = pygame.transform.scale(slugImg, (200,200))
slugImg2 = pygame.transform.flip(slugImg, True, False)

treesImg = pygame.image.load('trees.png')
treesImg = pygame.transform.scale(treesImg, (400,400))

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
        raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

    # need to use anti aliasing circle drawing routines to smooth the corners
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    rect_tmp = pygame.Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)
####################################################


def fade(screen, width, height, color): 
    fade = pygame.Surface((width, height))
    fade.fill(color)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)
        

def initalizeButtons(screen):
    #background
    screen.blit(treesImg, (0, 380))
    screen.blit(treesImg, (400, 380))
    
    #Start Button
    start_button = pygame.Rect(225,180,350,110)
    draw_rounded_rect(screen, start_button, blue, 20)
    start_button = pygame.Rect(215,170,370,130)
    draw_rounded_rect(screen, start_button, blue, 20)
    # How to Play button
    how_button = pygame.Rect(150,350,200,80)
    draw_rounded_rect(screen, how_button, orange, 15)
    how_button = pygame.Rect(140,340,220,100)
    draw_rounded_rect(screen, how_button, orange, 15)
    # Purpose Button
    purpose_button = pygame.Rect(450,350,200,80)
    draw_rounded_rect(screen, purpose_button, orange, 15)
    how_button = pygame.Rect(440,340,220,100)
    draw_rounded_rect(screen, how_button, orange, 15)

    #display images
    screen.blit(slugImg, (10, 125))
    screen.blit(slugImg2, (590, 125))


def restartHome(screen):
    screen.fill(cyan) #reset background color
    
    #reset title w/shadow
    myfont = pygame.font.SysFont('segoescript', 80)
    textsurface = myfont.render('Save the Slugs', True, blue)

    screen.blit(textsurface,(82,40))
    myfont = pygame.font.SysFont('segoescript', 80)
    textsurface = myfont.render('Save the Slugs', True, yellow)
    screen.blit(textsurface,(85,45))
    
    #reset all buttons with shadow
    initalizeButtons(screen)
    
def buttonInteractions(screen):
    
    mouse = pygame.mouse.get_pos() #get coordinates of mouse
    # if x-pos + width > .... > x-pos and y-pos + height > ... >y-pos
    
    #start screen button interactions
    if ((225 + 350) > mouse[0] > 225 ) and ((180 + 110) > mouse[1] > 180):
        start_button = pygame.Rect(225,180,350,110)
        draw_rounded_rect(screen, start_button, bright_blue, 20)

        click = pygame.mouse.get_pressed() #check on click
        if click[0]: #if mouse is clicked on star button
            status = Stages.playSammy(screen)
            
            if status == "home": #upon selection of home screen button
                restartHome(screen)
                pygame.display.update()
                return
        
    #how to button interaction
    elif ((150 + 200) > mouse[0] > 150 ) and ((350 + 80) > mouse[1] > 350): #how to button
        how_button = pygame.Rect(150,350,200,80)
        draw_rounded_rect(screen, how_button, bright_orange, 15)
        
        click = pygame.mouse.get_pressed() #check on click
        if click[0]: #if mouse is clicked on how to button
            fade(screen, 800,500, yellow) #fade to welcome screen

            #Back Button
            back_button = pygame.Rect(310,400,170,80)
            draw_rounded_rect(screen, back_button, blue, 15)
            back_shadow = pygame.Rect(300,390,190,100)
            draw_rounded_rect(screen, back_shadow, blue, 15)

            myfont = pygame.font.SysFont('Comic Sans MS', 55)# How to Play Title
            textsurface = myfont.render('How to Play', True, blue)
            screen.blit(textsurface,(260,20))
            #How To Text
            myfont = pygame.font.SysFont('corbel', 33)
            textsurface = myfont.render("How to play! Help save Sammy's friends and pick up", True, blue)
            screen.blit(textsurface,(65,120))
            textsurface = myfont.render("trash littered around the UCSC Campus! Navigate", True, blue)
            screen.blit(textsurface,(65,160))
            textsurface = myfont.render("yourself through the different parts of campus and", True, blue)
            screen.blit(textsurface,(65,200))
            textsurface = myfont.render("click on pieces of trash found in order to clean", True, blue)
            screen.blit(textsurface,(65,240))
            textsurface = myfont.render("up! Make sure to find Sammy and his friends for", True, blue)
            screen.blit(textsurface,(65,280))
            textsurface = myfont.render("extra bonus points!", True, blue)
            screen.blit(textsurface,(280,320))
            pygame.display.update()

            reading = True #user is reading how to
            cover_button = False #if button was pressed
            while reading:

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_var = pygame.mouse.get_pos() #get coordinates of mouse
                        if ((330 + 170) > mouse_var[0] > 330 ) and ((400 + 80) > mouse_var[1] > 400): #checks if mouse is over back button
                            #Back Button
                            back_button = pygame.Rect(310,400,170,80)
                            draw_rounded_rect(screen, back_button, bright_blue, 15)
                            cover_button = True #keeps track if mouse is clicked over the button
                        else:
                            draw_rounded_rect(screen, back_button, blue, 15) #regular back button color
                            
                    
                #Back Button Text
                myfont = pygame.font.SysFont('Comic Sans MS', 35)
                textsurface = myfont.render('Back', True, yellow) #Creating the Back Button
                screen.blit(textsurface, (350, 410) )

                pygame.display.update()

                click = pygame.mouse.get_pressed() #check if mouse is clicked           
                if cover_button and click[0]:  # if mouse clicked over back button
                    reading = False #end reading loop
                    restartHome(screen)

                    
   
    # purpose button interaction
    elif ((450 + 200) > mouse[0] > 450 ) and ((350 + 80) > mouse[1] > 350):
        purpose_button = pygame.Rect(450,350,200,80)
        draw_rounded_rect(screen, purpose_button, bright_orange, 15)
        
        click = pygame.mouse.get_pressed() #check on click
        if click[0]: #if mouse is clicked on how to button
            fade(screen, 800,500, yellow) #fade to welcome screen

            #How to Layout
            #Back Button
            back_button = pygame.Rect(310,400,170,80)
            draw_rounded_rect(screen, back_button, blue, 15)
            back_shadow = pygame.Rect(300,390,190,100)
            draw_rounded_rect(screen, back_shadow, blue, 15)
            
            myfont = pygame.font.SysFont('Comic Sans MS', 55)
            textsurface = myfont.render('Purpose', True, blue)  #title
            screen.blit(textsurface,(300,20))

            #How To Text
            myfont = pygame.font.SysFont('corbel', 33)# How to Play Text
            textsurface = myfont.render("Helping to clean up UCSC's campus will not only ensure", True, blue)
            screen.blit(textsurface,(45,105))
            textsurface = myfont.render("the survival of Sammy and his friends, but it will also", True, blue)
            screen.blit(textsurface,(45,145))
            textsurface = myfont.render("help to educate those about climate change and it's", True, blue)
            screen.blit(textsurface,(45,185))
            textsurface = myfont.render("slow but detrimental effects on the enivornment. By", True, blue)
            screen.blit(textsurface,(45,225))
            textsurface = myfont.render("advancing through the game we can see how pollution", True, blue)
            screen.blit(textsurface,(45,265))
            textsurface = myfont.render("affects climate change which causes huge ripple effects", True, blue)
            screen.blit(textsurface,(45,305))
            textsurface = myfont.render("felt around the world!", True, blue)
            screen.blit(textsurface,(260,345))
            pygame.display.update()
            
            reading = True #user is reading how to
            cover_button = False
            while reading:

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_var = pygame.mouse.get_pos() #get coordinates of mouse
                        if ((330 + 170) > mouse_var[0] > 330 ) and ((400 + 80) > mouse_var[1] > 400): #checks if mouse is over back button
                            #Back Button
                            back_button = pygame.Rect(310,400,170,80)
                            draw_rounded_rect(screen, back_button, bright_blue, 15)
                            
                            cover_button = True #keeps track if mouse is clicked over the button
                        else:
                            draw_rounded_rect(screen, back_button, blue, 15) #regular back button color
                            
                    
                #Back Button Text
                myfont = pygame.font.SysFont('Comic Sans MS', 35)
                textsurface = myfont.render('Back', True, yellow) #Creating the Back Button
                screen.blit(textsurface, (350, 410) )
            
                pygame.display.update()

                click = pygame.mouse.get_pressed() #check if mouse is clicked           
                if cover_button and click[0]:  # if mouse clicked over back button
                    reading = False #end reading loop
                    restartHome(screen)
    else:
        #Start Button
        start_button = pygame.Rect(225,180,350,110)
        draw_rounded_rect(screen, start_button, blue, 20)
        # How to Play button
        how_button = pygame.Rect(150,350,200,80)
        draw_rounded_rect(screen, how_button, orange, 15)
        # Purpose Button
        purpose_button = pygame.Rect(450,350,200,80)
        draw_rounded_rect(screen, purpose_button, orange, 15)
        
    buttonText(screen)


def buttonText(screen):

    #start button text
    myfont = pygame.font.SysFont('arialblack', 70)
    textsurface = myfont.render('START', True, yellow)
    screen.blit(textsurface,(275,182))
    #how to button text
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    textsurface = myfont.render('How to Play', True, yellow)
    screen.blit(textsurface, (158, 365) )
    #how to button text
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    textsurface = myfont.render('Purpose', True, yellow)
    screen.blit(textsurface, (490, 365) )





