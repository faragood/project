import pygame
import os
from pygame import mixer
import sys
pygame.init()
background = pygame.image.load("pictures/background.jpg")
background = pygame.transform.scale(background, (background.get_size()[0]//1.4, background.get_size()[1]//1.4))
background_rect = background.get_rect()

xx = background.get_size()[0]
yy = background.get_size()[1]

screen = pygame.display.set_mode((xx, yy))
pygame.display.set_caption("PHONK MACHINE")
font = pygame.font.Font(None, 36)
click = False
click_pause = False
click_play = False
click_next = False
click_previous = False
play = False
play_button0 = pygame.image.load("pictures/play.png")
play_button0 = pygame.transform.scale(play_button0, (play_button0.get_size()[0]//3, play_button0.get_size()[1]//3))
play_rect = play_button0.get_rect(topleft = (xx//2 - play_button0.get_size()[0]//2, yy//1.3 - play_button0.get_size()[1]//2))

pause_button0 = pygame.image.load("pictures/pause.png")
pause_button0 = pygame.transform.scale(pause_button0, (pause_button0.get_size()[0]//3, pause_button0.get_size()[1]//3))
pause_rect = pause_button0.get_rect(topleft = (xx//2 - pause_button0.get_size()[0]//2, yy//1.3 - pause_button0.get_size()[1]//2))

next_button0 = pygame.image.load("pictures/next.png")
next_button0 = pygame.transform.scale(next_button0, (next_button0.get_size()[0]//3, next_button0.get_size()[1]//3))
next_rect = next_button0.get_rect(topleft = (xx//2 - next_button0.get_size()[0]//2 + 100, yy//1.3 - next_button0.get_size()[1]//2))

previous_button0 = pygame.image.load("pictures/previous.png")
previous_button0 = pygame.transform.scale(previous_button0, (previous_button0.get_size()[0]//3, previous_button0.get_size()[1]//3))
previous_rect = previous_button0.get_rect(topleft = (xx//2 - previous_button0.get_size()[0]//2 - 100, yy//1.3 - previous_button0.get_size()[1]//2))

picture = pygame.image.load("pictures/phonk.jpg")
picture = pygame.transform.scale(picture, (picture.get_size()[0]//1.3, picture.get_size()[1]//1.3))
picture_rect = picture.get_rect(topleft = (xx//2 - picture.get_size()[0]//2, yy//3 - picture.get_size()[1]//2))

music_list0 = os.listdir(path = "music")
music_list = []
for i in music_list0:
    if i != ".DS_Store":
        music_list.append(i)
order = 0
x = 30
prev_x = 0
prev_time = 0
music = False
music_length = 1
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
set_music(order)
def play_button_blit():
    screen.blit(play_button0, play_rect)
def pause_button_blit():
    screen.blit(pause_button0, pause_rect)

while True:
    screen.blit(background, background_rect)
    screen.blit(next_button0, next_rect)
    screen.blit(previous_button0, previous_rect)
    screen.blit(picture, picture_rect)
    if not play:
        play_button_blit()
    else:
        pause_button_blit()
        
    if x >= xx - 31:
        x = 30
        prev_x = 0
        mixer.music.play()
        mixer.music.pause()
        play = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not play:
                    click_pause = True
                else:
                    click_play = True
            elif event.key == pygame.K_RIGHT:
                if order + 1 > len(music_list) - 1:
                    order = 0
                    set_music(order)
                    mixer.music.unpause()
                    play = True
                else:
                    order+=1
                    set_music(order)
                    mixer.music.unpause()
                    play = True
                click_next = False
            elif event.key == pygame.K_LEFT:
                if order - 1 < 0:
                    order = len(music_list) - 1
                    set_music(order)
                    mixer.music.unpause()
                    play = True
                else:
                    order-=1
                    set_music(order)
                    mixer.music.unpause()
                    play = True
                click_previous = False
    pygame.draw.circle(screen, (255, 255, 255), (x, yy//1.1), 20)
    pygame.draw.rect(screen, (50, 50, 50), (15, yy//1.1-7, xx-30, 15))
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[1] >= yy//1.1-20 and pygame.mouse.get_pos()[1] <= yy//1.1+20:
            click = True
        if (((pygame.mouse.get_pos()[0] - xx//2)**2 + (pygame.mouse.get_pos()[1] - yy//1.3)**2)**(1/2)) <= 30:
            if not play:
                click_pause = True
            else:
                click_play = True
        if (((pygame.mouse.get_pos()[0] - (xx//2 + 100))**2 + (pygame.mouse.get_pos()[1] - yy//1.3)**2)**(1/2)) <= 30:
            click_next = True
        if (((pygame.mouse.get_pos()[0] - (xx//2 - 100))**2 + (pygame.mouse.get_pos()[1] - yy//1.3)**2)**(1/2)) <= 30:
            click_previous = True
    if not pygame.mouse.get_pressed()[0]:
        if not music:
            prev_x = x-30
            mixer.music.play(start = music_length*((x-30)/(xx-60)))
            music = True
            play = True
        click = False
        if click_pause:
            mixer.music.unpause()
            play = True
            click_pause = False
        if click_play:
            mixer.music.pause()
            play = False
            click_play = False
        if click_next:
            if order + 1 > len(music_list) - 1:
                order = 0
                set_music(order)
                mixer.music.unpause()
                play = True
            else:
                order+=1
                set_music(order)
                mixer.music.unpause()
                play = True
            click_next = False
        if click_previous:
            if order - 1 < 0:
                order = len(music_list) - 1
                set_music(order)
                mixer.music.unpause()
                play = True
            else:
                order-=1
                set_music(order)
                mixer.music.unpause()
                play = True
            click_previous = False
    sec = round(music_length*((x-30)/(xx-60)))
    text = font.render("0" + str(sec//60) + ":" + "0"*(2-len(str(sec%60))) + str(sec%60), True, (50, 50, 50))
    screen.blit(text, (30, yy-30))
    
    sec1 = round(music_length - sec)
    text = font.render("0" + str(sec1//60) + ":" + "0"*(2-len(str(sec1%60))) + str(sec1%60), True, (50, 50, 50))
    screen.blit(text, (xx-80, yy-30))
    
    text = font.render(str(music_list[order]), True, (10, 10, 10))
    text_rec = text.get_rect(topleft = (xx//2 - text.get_size()[0]//2, yy//1.5 - text.get_size()[1]//2))
    screen.blit(text, text_rec)
    
    if mixer.music.get_busy() or not play:
        x = (mixer.music.get_pos()*0.001/music_length)*(xx-60)+30 + prev_x
    else:
        x = 30
    if click:
        if music:
            mixer.music.stop()
            music = False
        if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[0] <= xx - 30:
            x = pygame.mouse.get_pos()[0]
    pygame.draw.circle(screen, (50, 50, 50), (x, yy//1.1), 20)
    pygame.draw.circle(screen, (255, 255, 255), (x, yy//1.1), 15)
    mouse_buttons = pygame.mouse.get_pressed()
    pygame.display.update()
    pygame.time.delay(40)
