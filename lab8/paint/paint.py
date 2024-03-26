import pygame
import sys
import os
pygame.init()

xx = 900
yy = 700
hotbar_x = 120
screen = pygame.display.set_mode((xx, yy))
draw = False
hotbar_click = False
prev_сoor = (0, 0)
radius = 3
x_red = 100
x_green = 90
x_blue = 255
color = (x_red, x_green, x_blue)
ctrl_k = False
z_k = False
y_k = False
ctrl_z = True

def delfiles(start):
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, 'screenshots')
    files = os.listdir(folder_path)
    file_number = 0
    for file in files:
        file_name = os.path.basename(file)
        if file_name[-4:] == ".png":
            file_number+=1
    for i in range(start, file_number+1):
        os.remove(os.path.join(folder_path, "screenshot" + str(i) + ".png"))
delfiles(1)

screenshot_number = 1
screenshot_curr = 1
pygame.image.save(screen, "screenshots/screenshot1.png")
    
def screenshot(screenshot_num, screenshot_cur):
    global screenshot_number
    global screenshot_curr
    global ctrl_z
    ctrl_z = True
    if screenshot_curr < screenshot_number:
        delfiles(screenshot_curr+1)
        screenshot_num = screenshot_cur
    screenshot_curr = screenshot_cur + 1
    screenshot_number = screenshot_num + 1
    pygame.image.save(screen, "screenshots/screenshot" + str(screenshot_curr) +".png")

def y(x, x0, x1, y0, y1):
    y_return = (x - x0)*(y1 - y0)/(x1 - x0) + y0
    return y_return


screen.fill((255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                delfiles(1)
                running = False
            elif event.key == pygame.K_LCTRL:
                ctrl_k = True
            elif event.key == pygame.K_z:
                z_k = True
            elif event.key == pygame.K_y:
                y_k = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                ctrl_k = False
            elif event.key == pygame.K_z:
                z_k = False
            elif event.key == pygame.K_y:
                y_k = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.mouse.get_pos()[0] > hotbar_x:
                    draw = True
                    screenshot(screenshot_number, screenshot_curr)
                else:
                    hotbar_click = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                draw = False
                hotbar_click = False
    
    color = (x_red, x_green, x_blue)

    if ctrl_k and z_k:
        if ctrl_z:
            screenshot(screenshot_number, screenshot_curr)
            screenshot_curr-=1
            ctrl_z = False
        if screenshot_curr > 1:
            image = pygame.image.load(os.path.join("screenshots", "screenshot" + str(screenshot_curr) + ".png"))
            screen.blit(image, (0, 0))
            screenshot_curr-=1
        z_k = False

    if ctrl_k and y_k:
        if screenshot_curr < screenshot_number:
            image = pygame.image.load(os.path.join("screenshots", "screenshot" + str(screenshot_curr+1) + ".png"))
            screen.blit(image, (0, 0))
            screenshot_curr+=1
        y_k = False
        
    if draw:
        current_coor = pygame.mouse.get_pos()
        if current_coor == prev_сoor:
            pygame.draw.circle(screen, color, current_coor, radius)
        else:
            mode = 1
            if abs(current_coor[0] - prev_сoor[0]) > abs(current_coor[1] - prev_сoor[1]):
                mode = 0
            step = 1
            if current_coor[mode] < prev_сoor[mode]:
                step = -1
            for i in range(prev_сoor[mode], current_coor[mode], step):
                if mode == 0:
                    pygame.draw.circle(screen, color, (i, y(i, prev_сoor[0], current_coor[0], prev_сoor[1], current_coor[1])), radius)
                else:
                    pygame.draw.circle(screen, color, (y(i, prev_сoor[1], current_coor[1], prev_сoor[0], current_coor[0]), i), radius)
    prev_сoor = pygame.mouse.get_pos()
    
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 0, hotbar_x, yy))
    for i in range(255, 0, -1):
        pygame.draw.rect(screen, (i, 0, 0), pygame.Rect(hotbar_x//4-7, 20+i, 14, 1))
    pygame.draw.circle(screen, (140, 140, 140), (hotbar_x//4, 20+x_red), 12)
    pygame.draw.circle(screen, (x_red, 0, 0), (hotbar_x//4, 20+x_red), 10)
    for i in range(255, 0, -1):
        pygame.draw.rect(screen, (0, i, 0), pygame.Rect(hotbar_x//4*2-7, 20+i, 14, 1))
    pygame.draw.circle(screen, (140, 140, 140), (hotbar_x//4*2, 20+x_green), 12)
    pygame.draw.circle(screen, (0, x_green, 0), (hotbar_x//4*2, 20+x_green), 10)
    for i in range(255, 0, -1):
        pygame.draw.rect(screen, (0, 0, i), pygame.Rect(hotbar_x//4*3-7, 20+i, 14, 1))
    pygame.draw.circle(screen, (140, 140, 140), (hotbar_x//4*3, 20+x_blue), 12)
    pygame.draw.circle(screen, (0, 0, x_blue), (hotbar_x//4*3, 20+x_blue), 10)
    pygame.display.flip()
    pygame.time.wait(10)

