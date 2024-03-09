#import all libraries and init them
import pygame
import os
from pygame import mixer
import sys
pygame.init()

#set backgroung image and change it size
background = pygame.image.load("pictures/background.jpg")
background = pygame.transform.scale(background, (background.get_size()[0]//1.4, background.get_size()[1]//1.4))
background_rect = background.get_rect()

#set screen size based on backround image's size
xx = background.get_size()[0]
yy = background.get_size()[1]
screen = pygame.display.set_mode((xx, yy))
pygame.display.set_caption("PHONK MACHINE")

#set font for all text
font = pygame.font.Font(None, 36)

#load play button and set it size
play_button0 = pygame.image.load("pictures/play.png")
play_button0 = pygame.transform.scale(play_button0, (play_button0.get_size()[0]//3, play_button0.get_size()[1]//3))
play_rect = play_button0.get_rect(topleft = (xx//2 - play_button0.get_size()[0]//2, yy//1.3 - play_button0.get_size()[1]//2))

#load pause button and set it size
pause_button0 = pygame.image.load("pictures/pause.png")
pause_button0 = pygame.transform.scale(pause_button0, (pause_button0.get_size()[0]//3, pause_button0.get_size()[1]//3))
pause_rect = pause_button0.get_rect(topleft = (xx//2 - pause_button0.get_size()[0]//2, yy//1.3 - pause_button0.get_size()[1]//2))

#load next button and set it size
next_button0 = pygame.image.load("pictures/next.png")
next_button0 = pygame.transform.scale(next_button0, (next_button0.get_size()[0]//3, next_button0.get_size()[1]//3))
next_rect = next_button0.get_rect(topleft = (xx//2 - next_button0.get_size()[0]//2 + 100, yy//1.3 - next_button0.get_size()[1]//2))

#load previous button and set it size
previous_button0 = pygame.image.load("pictures/previous.png")
previous_button0 = pygame.transform.scale(previous_button0, (previous_button0.get_size()[0]//3, previous_button0.get_size()[1]//3))
previous_rect = previous_button0.get_rect(topleft = (xx//2 - previous_button0.get_size()[0]//2 - 100, yy//1.3 - previous_button0.get_size()[1]//2))

#load phonk picture button and set it size
picture = pygame.image.load("pictures/phonk.jpg")
picture = pygame.transform.scale(picture, (picture.get_size()[0]//1.3, picture.get_size()[1]//1.3))
picture_rect = picture.get_rect(topleft = (xx//2 - picture.get_size()[0]//2, yy//3 - picture.get_size()[1]//2))

#set all variables
click = False #variable checks for mouse click
click_pause = False #variable checks if pause button have been clicked
click_play = False #variable checks if play button have been clicked
click_next = False #variable checks if next button have been clicked
click_previous = False #variable checks if previous button have been clicked
play = False #variable checks if music is paused
music = False #variable checks if music is playing
order = 0 #variable shows track queue
x = 30 #variable shows the coordinate of the slider
prev_x = 0 #variable shows the previous coordinate of the slider
prev_time = 0 #variable shows the previous value of the track time
music_length = 1 #variable shows the lenght of the track

#get list of tracks in /music/ folder
music_list0 = os.listdir(path = "music")
music_list = []
for i in music_list0:
    if i != ".DS_Store":
        music_list.append(i)

#function to set new track
def set_music(order):
    global music_length
    music_length = mixer.Sound("music/" + music_list[order]).get_length()
    mixer.music.load("music/" + music_list[order])
    mixer.music.play()
    mixer.music.pause()
    global music
    global prev_x
    global prev_time
    global x
    music = True
    prev_x = 0
    prev_time = 0
    x = 30

#set first track in que
set_music(order)

#function to draw play button
def play_button_blit():
    screen.blit(play_button0, play_rect)

#function to draw pause button
def pause_button_blit():
    screen.blit(pause_button0, pause_rect)

#main loop
while True:
    #draw all elements on the screen---------------------------------
    screen.blit(background, background_rect) #backgroung
    screen.blit(next_button0, next_rect) #next_button
    screen.blit(previous_button0, previous_rect) #previous button
    screen.blit(picture, picture_rect) #phonk picture
    pygame.draw.rect(screen, (50, 50, 50), (15, yy//1.1-7, xx-30, 15)) #track of slider
    pygame.draw.circle(screen, (50, 50, 50), (x, yy//1.1), 20)
    pygame.draw.circle(screen, (255, 255, 255), (x, yy//1.1), 15)
    
    #print current position of the track
    sec = round(music_length*((x-30)/(xx-60)))
    text = font.render("0" + str(sec//60) + ":" + "0"*(2-len(str(sec%60))) + str(sec%60), True, (50, 50, 50))
    screen.blit(text, (30, yy-30))
    
    #print remaining track time
    sec1 = round(music_length - sec)
    text = font.render("0" + str(sec1//60) + ":" + "0"*(2-len(str(sec1%60))) + str(sec1%60), True, (50, 50, 50))
    screen.blit(text, (xx-80, yy-30))
    
    #print track name
    text = font.render(str(music_list[order]), True, (10, 10, 10))
    text_rec = text.get_rect(topleft = (xx//2 - text.get_size()[0]//2, yy//1.5 - text.get_size()[1]//2))
    screen.blit(text, text_rec)
    
    #draw play button if music paused or draw pause button if music is not paused
    if not play:
        play_button_blit()
    else:
        pause_button_blit()
    
    pygame.display.update() #update screen
    #----------------------------------------------------------------
        
    #if track has been ended, set it again
    if x >= xx - 31:
        x = 30
        prev_x = 0
        mixer.music.play()
        mixer.music.pause()
        play = False
    
    #check for all keyboard events
    for event in pygame.event.get():
        #quit loop
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            #pauses music if SPACE have been pressed
            if event.key == pygame.K_SPACE:
                if not play:
                    click_pause = True
                else:
                    click_play = True
            #sets next track if RIGHT have been pressed
            elif event.key == pygame.K_RIGHT:
                if order + 1 > len(music_list) - 1:
                    order = 0
                else:
                    order+=1
                set_music(order)
                mixer.music.unpause()
                play = True
                click_next = False
            #sets previous track if LEFT have been pressed
            elif event.key == pygame.K_LEFT:
                if order - 1 < 0:
                    order = len(music_list) - 1
                else:
                    order-=1
                set_music(order)
                mixer.music.unpause()
                play = True
                click_previous = False
    
    #checks if mouse have been pressed
    if pygame.mouse.get_pressed()[0]:
        #checks if slider button have been pressed and then waits when it will be released
        if pygame.mouse.get_pos()[1] >= yy//1.1-20 and pygame.mouse.get_pos()[1] <= yy//1.1+20:
            click = True
        #checks if pause/play button have been pressed and then waits when it will be released
        if (((pygame.mouse.get_pos()[0] - xx//2)**2 + (pygame.mouse.get_pos()[1] - yy//1.3)**2)**(1/2)) <= 30:
            if not play:
                click_pause = True
            else:
                click_play = True
        #checks if next button have been pressed and then waits when it will be released
        if (((pygame.mouse.get_pos()[0] - (xx//2 + 100))**2 + (pygame.mouse.get_pos()[1] - yy//1.3)**2)**(1/2)) <= 30:
            click_next = True
        #checks if previous button have been pressed and then waits when it will be released
        if (((pygame.mouse.get_pos()[0] - (xx//2 - 100))**2 + (pygame.mouse.get_pos()[1] - yy//1.3)**2)**(1/2)) <= 30:
            click_previous = True
            
    #checks if mouse button is released
    if not pygame.mouse.get_pressed()[0]:
        #set new position of the track
        if click:
            prev_x = x-30
            mixer.music.play(start = music_length*((x-30)/(xx-60)))
            music = True
            play = True
            click = False
        #unpause music
        if click_pause:
            mixer.music.unpause()
            play = True
            click_pause = False
        #pause music
        if click_play:
            mixer.music.pause()
            play = False
            click_play = False
        #set next track
        if click_next:
            if order + 1 > len(music_list) - 1:
                order = 0
            else:
                order+=1
            set_music(order)
            mixer.music.unpause()
            play = True
            click_next = False
        #set previous track
        if click_previous:
            if order - 1 < 0:
                order = len(music_list) - 1
            else:
                order-=1
            set_music(order)
            mixer.music.unpause()
            play = True
            click_previous = False
            
    #set new position of x based on current track time
    if mixer.music.get_busy() or not play:
        x = (mixer.music.get_pos()*0.001/music_length)*(xx-60)+30 + prev_x
    else:
        x = 30
    
    #stops music while slider button click and sets new position of x
    if click:
        if music:
            mixer.music.stop()
            music = False
        if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[0] <= xx - 30:
            x = pygame.mouse.get_pos()[0]
    
    pygame.time.delay(40) #wait for 40ms (25 fps)
