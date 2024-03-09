import pygame
import sys
pygame.init()
xx = 775
yy = 775
screen = pygame.display.set_mode((xx, yy))
gameOn = True

x = xx//2
y = yy//2
r = 25
step = 20

def check(x, y):
    if x+r <= xx and x-r >= 0 and y+r <= yy and y-r >= 0:
        return True
        
while gameOn:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameOn = False
                
            elif event.key == pygame.K_RIGHT:
                x1 = x + step
                if check(x1, y):
                    x = x1
        
            elif event.key == pygame.K_LEFT:
                x1 = x - step
                if check(x1, y):
                    x = x1
            
            elif event.key == pygame.K_UP:
                y1 = y - step
                if check(x, y1):
                    y = y1
            
            elif event.key == pygame.K_DOWN:
                y1 = y + step
                if check(x, y1):
                    y = y1

    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    pygame.display.update()
    pygame.time.delay(40)
