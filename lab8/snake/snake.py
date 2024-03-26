import pygame
from random import randint
import sys
import math
from pygame.locals import *
pygame.init()
x = 35
y = 24

xx = x*30
yy = y*30
screen = pygame.display.set_mode((xx, yy))
gameOn = True
dir = "+y"
cor  = [(0, 1), (0, 2)]
leng = len(cor)
time = 0
speed = 5
cof = 1.025
xr = randint(0, xx//30-1)
yr = randint(0, yy//30-1)
score = 0
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Score: " + str(score), True, (0, 0, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (xx-110, 20)
screen.blit(text, textRect)
click = 1

while True:
    if (xr, yr) not in cor:
        break;
    else:
        xr = randint(0, xx//30-1)
        yr = randint(0, yy//30-1)
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(xr*30, yr*30, 28, 28))
for i in cor:
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i[0]*30, i[1]*30, 28, 28))
    pygame.display.flip()

while gameOn:
    pygame.time.wait(5)
    time += speed
    for event in pygame.event.get():
        if click == 1:
            keys = pygame.key.get_pressed()
            if dir[1] != "y":
                if keys[pygame.K_w]:
                    dir = "-y"
                if keys[pygame.K_s]:
                    dir = "+y"
            else:
                if keys[pygame.K_d]:
                    dir = "+x"
                if keys[pygame.K_a]:
                    dir = "-x"
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    gameOn = False
            click = 1
    if time >= 150:
        plus = set()
        if dir == "-y":
            plus = (cor[len(cor)-1][0], cor[len(cor)-1][1] -1)
        elif dir == "+y":
            plus = (cor[len(cor)-1][0], cor[len(cor)-1][1] +1)
        elif dir == "-x":
            plus = (cor[len(cor)-1][0] - 1, cor[len(cor)-1][1])
        elif dir == "+x":
            plus = (cor[len(cor)-1][0]+1, cor[len(cor)-1][1])
        if plus not in cor:
            cor.append(plus)
        elif plus == cor[len(cor) - 2]:
            if dir == "-y":
                plus = (cor[len(cor)-1][0], cor[len(cor)-1][1] +1)
                dir = "+y"
            elif dir == "+y":
                plus = (cor[len(cor)-1][0], cor[len(cor)-1][1] -1)
                dir = "-y"
            elif dir == "-x":
                plus = (cor[len(cor)-1][0] + 1, cor[len(cor)-1][1])
                dir = "+x"
            elif dir == "+x":
                plus = (cor[len(cor)-1][0]-1, cor[len(cor)-1][1])
                dir = "-x"
            cor.append(plus)
        else:
            font = pygame.font.Font('freesansbold.ttf', 70)
            text = font.render("Score: " + str(score), True, (0, 0, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (xx//2, yy//2)
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.time.wait(2000)
            gameOn = False
        if cor[len(cor)-1][0] > xx//30-1:
            cor[len(cor)-1] = (0, cor[len(cor)-1][1])
        if cor[len(cor)-1][0] < 0:
            cor[len(cor)-1] = (xx//30-1, cor[len(cor)-1][1])
        if cor[len(cor)-1][1] > yy//30-1:
            cor[len(cor)-1] = (cor[len(cor)-1][0], 0)
        if cor[len(cor)-1][1] < 0:
            cor[len(cor)-1] = (cor[len(cor)-1][0], yy//30-1)
        if len(cor) > leng:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(cor[0][0]*30, cor[0][1]*30, 28, 28))
            cor.pop(0)
        if cor[len(cor)-1][0] == xr and cor[len(cor)-1][1] == yr:
            leng+=1
            speed*=cof
            score+=1
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(xr*30, yr*30, 28, 28))
            while True:
                if (xr, yr) not in cor:
                    break;
                else:
                    xr = randint(0, xx//30-1)
                    yr = randint(0, yy//30-1)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(xr*30, yr*30, 28, 28))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(cor[len(cor)-1][0]*30, cor[len(cor)-1][1]*30, 28, 28))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Score: " + str(score), True, (0, 0, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (xx-110, 20)
        screen.blit(text, textRect)
        pygame.display.flip()
        time = 0
        click = 1

