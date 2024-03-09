#import all libraries and init them
import pygame
import sys
pygame.init()

#set size of screen
xx = 775
yy = 775
screen = pygame.display.set_mode((xx, yy))

#set coordinates of circle in the center of the screen, radius of circle and step size
x = xx//2
y = yy//2
r = 25
step = 20

#function for checking if circle coordinates will go out of border
def check(x, y):
    if x+r <= xx and x-r >= 0 and y+r <= yy and y-r >= 0:
        return True

#Main loop
gameOn = True
while gameOn:

    #check for events
    for event in pygame.event.get():
        #check for clicks on keyboard
        if event.type == pygame.KEYDOWN:
            #if q is clicked quit loop
            if event.key == pygame.K_q:
                gameOn = False
            #if RIGHT is clicked move circle right
            elif event.key == pygame.K_RIGHT:
                x1 = x + step
                if check(x1, y):
                    x = x1
            #if LEFT is clicked move circle left
            elif event.key == pygame.K_LEFT:
                x1 = x - step
                if check(x1, y):
                    x = x1
            #if UP is clicked move circle up
            elif event.key == pygame.K_UP:
                y1 = y - step
                if check(x, y1):
                    y = y1
            #if DOWN is clicked move circle down
            elif event.key == pygame.K_DOWN:
                y1 = y + step
                if check(x, y1):
                    y = y1
    
    #draw all elements and update screen
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    pygame.display.update()
    
    #wait for 40ms (25 fps)
    pygame.time.delay(40)
