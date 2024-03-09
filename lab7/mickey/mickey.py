#import all libraries and init them
import pygame
import sys
from pygame.locals import K_q
from datetime import datetime, timedelta
pygame.init()

#set size for screen (0.7 = 70% of original image)
siz = 0.7

#Add and set size for Mickey's body
image_body0 = pygame.image.load("images/mainclock.png")
image_body = pygame.transform.scale(image_body0, (image_body0.get_size()[0]//(siz**(-1)), image_body0.get_size()[1]//(siz**(-1))))
image_body_rect = image_body.get_rect()

#Set size of screen based on size of Mickey's body
x = image_body0.get_size()[0]//(siz**(-1))
y = image_body0.get_size()[1]//(siz**(-1))
screen = pygame.display.set_mode((x, y))

#Add and set size for Mickey's left arm
image_leftarm0 = pygame.image.load("images/leftarm.png")
image_leftarm0 = pygame.transform.scale(image_leftarm0, (image_leftarm0.get_size()[0]//(siz**(-1)), image_leftarm0.get_size()[1]//(siz**(-1))))

#Add and set size for Mickey's right arm
image_rightarm0 = pygame.image.load("images/rightarm.png")
image_rightarm0 = pygame.transform.scale(image_rightarm0, (image_rightarm0.get_size()[0]//(siz**(-1)), image_rightarm0.get_size()[1]//(siz**(-1))))

#Get current time and set angles for sec and min arrows
date = datetime.now()
sec = int(date.strftime("%S"))
min = int(date.strftime("%M"))
angle_sec = -4 -sec*6
angle_min = -54 -min*6

#Main loop
gameOn = True
while gameOn:
    #Event for end loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                gameOn = False
    
    #Turn left arm and set it in center
    image_leftarm = pygame.transform.rotate(image_leftarm0, angle_sec)
    image_leftarm_rect = image_body.get_rect(topleft=(x//2- image_leftarm.get_size()[0]//2, y//2-image_leftarm.get_size()[1]//2))
        
    #Turn right arm and set it in center
    image_rightarm = pygame.transform.rotate(image_rightarm0, angle_min)
    image_rightarm_rect = image_body.get_rect(topleft=(x//2- image_rightarm.get_size()[0]//2, y//2-image_rightarm.get_size()[1]//2))
    
    #Draw all elements on the screen
    screen.fill((255, 255, 255))
    screen.blit(image_body, image_body_rect)
    screen.blit(image_leftarm, image_leftarm_rect)
    screen.blit(image_rightarm, image_rightarm_rect)
    pygame.display.flip()
    
    #Wait for 1000ms and then set new values for sec and min angles
    pygame.time.delay(1000)
    angle_sec-=6
    sec+=1
    if sec == 60:
        sec = 0
        angle_min-=6

