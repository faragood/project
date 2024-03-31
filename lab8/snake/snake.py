#import all libraries and init them
import pygame
from random import randint
import sys
pygame.init()

#inital variables for display setting
x = 35 #numer of cells for width
y = 24 #number of cells for heigth
xx = x*30 #width of the screen based on x cells(each cell has size of 30x30 pixels)
yy = y*30 #heigth of the screen based on y cells(each cell has size of 30x30 pixels)
screen = pygame.display.set_mode((xx, yy)) #set display

#function for loss
def loss(xx, yy, score):
    font = pygame.font.Font('freesansbold.ttf', 32) #set font
    text = font.render("You lose! Score: " + str(score), True, (0, 180, 0)) #"You lose!"
    text_rec = text.get_rect(topleft = (xx//2 - text.get_size()[0]//2, yy//2 - text.get_size()[1]//2)) #set location for "You lose!"
    screen.blit(text, text_rec) #blit text
    text = font.render("(SPACE to restart)", True, (0, 180, 0)) #"SPACE to restart"
    text_rec = text.get_rect(topleft = (xx//2 - text.get_size()[0]//2, yy//1.8 - text.get_size()[1]//2)) #set location for "SPACE to restart"
    screen.blit(text, text_rec) #blit text
    pygame.display.update() #update screen

    #wait until player will quit the game or will press 'ESCAPE' for quit game or 'SPACE' to start new game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() #quit the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    game(xx, yy) #start new game
                elif event.key == pygame.K_ESCAPE:
                    exit() #quit the game
        pygame.time.delay(50) #wait for 50ms

#function for game
def game(xx, yy):
    dir = "+y" #direction of the snake
    cor  = [(0, 1), (0, 2)] #coordinates of cells of snake
    leng = len(cor) #length of snake
    time = 0 #variable for ticking time to start next frame
    speed = 5 #speed of game processes
    cof = 1.07 #coeficient of speed increasing
    global xr, yr #global variables 'xr' and 'yr'
    xr = 0 #x coordinate of food
    yr = 0 #y coordinate of food
    score = 0 #players score
    level = 0 #game level
    next_move = True #variable for noticing keyboard events
    pygame.display.set_caption('snake') #set name for game window
    font = pygame.font.Font('freesansbold.ttf', 32) #font for text
    
    #blit all inital cells of snake
    for i in cor:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i[0]*30, i[1]*30, 28, 28))
        pygame.display.flip()
    
    #function for random generating food
    def food_gen(cor):
        xrr = randint(0, xx//30-1) #get random x coordinate
        yrr = randint(0, yy//30-1) #get random y coordinate
        global xr, yr #global variables 'xr' and 'yr'
        #if food coordinates inside of snake, set new value until it will be outside
        while True:
            if (xrr, yrr) not in cor:
                break;
            else:
                xrr = randint(0, xx//30-1)
                yrr = randint(0, yy//30-1)
        xr = xrr #set new value for xr
        yr = yrr #set new value for yr
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(xrr*30, yrr*30, 28, 28)) #draw new position of food
        
    food_gen(cor) #generate initial food
    
    #main loop
    gameOn = True
    while gameOn:
        #get all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() #quit the game
            elif event.type == pygame.KEYDOWN: #check for KEYDOWN EVENTS
                if next_move: #wait until next_move will be True
                    if event.key == pygame.K_ESCAPE:
                        exit() #quit the game for ESCAPE
                    #set new direction for snake
                    elif dir[1] != "y":
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            dir = "-y"
                        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                            dir = "+y"
                    else:
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            dir = "+x"
                        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            dir = "-x"
                    next_move = False #set next_move to False(with next cycle it will become True)
                    
        if time >= 150: #wait untill 'time' will reach 150
            plus = set() #make variable for the new position of snake's head
            #based on snake direction set value for 'plus'
            if dir == "-y":
                plus = (cor[len(cor)-1][0], cor[len(cor)-1][1] -1)
            elif dir == "+y":
                plus = (cor[len(cor)-1][0], cor[len(cor)-1][1] +1)
            elif dir == "-x":
                plus = (cor[len(cor)-1][0] - 1, cor[len(cor)-1][1])
            elif dir == "+x":
                plus = (cor[len(cor)-1][0]+1, cor[len(cor)-1][1])
            next_move = True
            
            #check if new position of snake's head is not inside of snake's body, else summon loss function
            if plus not in cor:
                cor.append(plus) #add new value for snake
            else:
                loss(xx, yy, score) #loss function
            
            #check if snake go out of border, then move it to the new position
            if cor[len(cor)-1][0] > xx//30-1:
                cor[len(cor)-1] = (0, cor[len(cor)-1][1])
            if cor[len(cor)-1][0] < 0:
                cor[len(cor)-1] = (xx//30-1, cor[len(cor)-1][1])
            if cor[len(cor)-1][1] > yy//30-1:
                cor[len(cor)-1] = (cor[len(cor)-1][0], 0)
            if cor[len(cor)-1][1] < 0:
                cor[len(cor)-1] = (cor[len(cor)-1][0], yy//30-1)
            
            if len(cor) > leng: #if current length of snake is greater than real, then delete last element of snake's cells list
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(cor[0][0]*30, cor[0][1]*30, 28, 28)) #draw black square insted of last element of snake's cells list
                cor.pop(0) #delete last element of snake's cells list
            
            #check if snake touched food
            if cor[len(cor)-1][0] == xr and cor[len(cor)-1][1] == yr:
                leng+=1 #add 1 to snake's real length
                speed*=cof #increase the speed
                score+=1 #add 1 to player score
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(xr*30, yr*30, 28, 28)) #draw black square instead of last position of the food
                food_gen(cor) #generate new food
            
            level = score//4 #set new value for level
            text = font.render("Score: " + str(score) + " Lvl: " + str(level), True, (0, 0, 255)) #text for score and level blit
            text_rect = text.get_rect(topleft = (xx - text.get_size()[0], 20 - text.get_size()[1]//2)) #set position for text
            pygame.draw.rect(screen, (0, 0, 0), text_rect) #draw black rectangle on the background of text
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(cor[len(cor)-1][0]*30, cor[len(cor)-1][1]*30, 28, 28)) #draw new position of snake's head
            screen.blit(text, text_rect) #blit the text
            
            pygame.display.flip()#update screen
            time = 0 #set time value to 0
            
        pygame.time.wait(5) #wait for 5ms
        time += speed #add to 'time' variable value of 'speed'
        
game(xx, yy)#inital start of the game
