#import all libraries and init them
import pygame
import sys
import os
pygame.init()

#all variables
font = pygame.font.Font(None, 30) #font for all text
size_change_text = font.render("+5", True, (50, 50, 50)) #text of size change buttons
infoObject = pygame.display.Info() #get information about display size
xx = infoObject.current_w #set width equal to width of display
yy = infoObject.current_h #set heigth equal to heigth of display
hotbar_x = 120 #size of hotbar
shapes_initial_coor = (0, 0) #inital coordinate for shapes drawing 
tool = 0 #position of tool
prev_сoor = (0, 0) #previous coordinate of mouse(used for drawing)
radius = 5 #radius of drawing circle
x_red = 0 #position for red color
x_green = 0 #position for green color
x_blue = 0 #position for blue color
color = (x_red, x_green, x_blue) #color of drawing
color_buttons = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (128, 0, 128), (255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 165, 0)
, (255, 192, 203), (127, 255, 0), (0, 255, 255), (128, 0, 128), (0, 255, 0), (0, 128, 128), (0, 0, 128), (192, 192, 192), (165, 42, 42)
] #list of initial colors in hotbar 
ctrl_k = False #variable checks if user clicked at LCTRL
z_k = False #variable checks if user clikced at 'z'
y_k = False #variable checks if user clicked 'y'
ctrl_z = True #variable checks if user cliked LCTRL and 'z'
red_click = False #variable checks if user cliked at red color slider
green_click = False #variable checks if user cliked at green color slider
blue_click = False #variable checks if user cliked at blue color slider
color_click = False #variable checks if user cliked at color selection slider
hotbar_click = False #variable checks if user clicked at hotbar
draw = False #variable checks if user drawing or not
shapes_draw = False #variable checks if user drawing shapes or not
screenshot_number = 1 #total number of screenshots
screenshot_curr = 1 #number of current screenshot 

screen = pygame.display.set_mode((xx, yy), pygame.FULLSCREEN) #set display 

pygame.image.save(screen, "screenshots/screenshot1.png") #save current screen

#load red scale picture
red_scale = pygame.image.load("png/red.png")
red_scale_rect = red_scale.get_rect(topleft = (hotbar_x//4-7, 20))

#load green scale picture
green_scale = pygame.image.load("png/green.png")
green_scale_rect = green_scale.get_rect(topleft = (hotbar_x//4*2-7, 20))

#load blue scale picture
blue_scale = pygame.image.load("png/blue.png")
blue_scale_rect = blue_scale.get_rect(topleft = (hotbar_x//4*3-7, 20))

#load tassel and set its size
tassel = pygame.image.load("png/tassel.png")
tassel = pygame.transform.scale(tassel, (30, 30))
tassel_rect = tassel.get_rect(topleft = (hotbar_x//3 - tassel.get_size()[0]//2, 650))

#load eraser and set its size
eraser = pygame.image.load("png/eraser.png")
eraser = pygame.transform.scale(eraser, (30, 30))
eraser_rect = eraser.get_rect(topleft = (hotbar_x//3*2 - eraser.get_size()[0]//2, 650))

#load circle and set its size
circle_0 = pygame.image.load("png/circle.png")
circle_0 = pygame.transform.scale(circle_0, (30, 30))
circle_0_rect = circle_0.get_rect(topleft = (hotbar_x//3 - circle_0.get_size()[0]//2, 695))

#load rectangle and set its size
rectangle_0 = pygame.image.load("png/rectangle.png")
rectangle_0 = pygame.transform.scale(rectangle_0, (30, 30))
rectangle_0_rect = rectangle_0.get_rect(topleft = (hotbar_x//3*2 - rectangle_0.get_size()[0]//2, 695))

#load square and set its size
square_0 = pygame.image.load("png/square.png")
square_0 = pygame.transform.scale(square_0, (30, 30))
square_0_rect = square_0.get_rect(topleft = (hotbar_x//3 - rectangle_0.get_size()[0]//2, 695+45))

#load right triangle and set its size
right_triangle = pygame.image.load("png/right_triangle.png")
right_triangle = pygame.transform.scale(right_triangle, (30, 30))
right_triangle_rect = right_triangle.get_rect(topleft = (hotbar_x//3*2 - right_triangle.get_size()[0]//2, 695+45))

#load equilateral triangle and set its size
equilateral_triangle = pygame.image.load("png/equilateral_triangle.png")
equilateral_triangle = pygame.transform.scale(equilateral_triangle, (30, 30))
equilateral_triangle_rect = equilateral_triangle.get_rect(topleft = (hotbar_x//3 - equilateral_triangle.get_size()[0]//2, 695+45*2))


#function draw size change buttons
def size_change_button(text, x_pos, y_pos, hotbar_x, font):
    size_change_text = font.render(text, True, (50, 50, 50))
    size_change_text_rec = size_change_text.get_rect(topleft = (hotbar_x//3*x_pos - size_change_text.get_size()[0]//2, y_pos))
    pygame.draw.rect(screen, (200, 200, 200), size_change_text_rec)
    screen.blit(size_change_text, size_change_text_rec)

#function checks if tool selection button was clicked
def tool_button_check(tool, hotbar_x):
    if pygame.mouse.get_pos()[0] >= hotbar_x//3*(tool%2 + 1) - 15 and pygame.mouse.get_pos()[0] <= hotbar_x//3*(tool%2 + 1) + 15 and pygame.mouse.get_pos()[1] >= 650 + (tool//2)*45 and pygame.mouse.get_pos()[1] <= 680 + (tool//2)*45:
        return True
    else:
        return False

#function checks if size change button was clicked
def size_change_button_check(dif, x_pos, y_pos, hotbar_x):
    global radius
    wid = 0
    if dif > 0:
        wid = 23
    else:
        wid = 18
    if pygame.mouse.get_pos()[0] >= hotbar_x//3*x_pos - wid//2 and pygame.mouse.get_pos()[0] <= hotbar_x//3*x_pos - wid//2 + wid and pygame.mouse.get_pos()[1] >= y_pos and pygame.mouse.get_pos()[1] <= y_pos + 20:
        if radius+dif >= 1 and radius+dif <=100:
            radius+=dif
        elif radius+dif < 1:
            radius = 1
        elif radius+dif > 100:
            radius = 100

#function deletes certain range of screenshots in "screenshots" folder
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
delfiles(2) #delete all screenshots
    
#function makes screenshot
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

#function finds second coordinate(given one coordinate) on line given by two points: (x0, y0) and (x1, y1)
def y(x, x0, x1, y0, y1):
    y_return = (x - x0)*(y1 - y0)/(x1 - x0) + y0
    return y_return

#function checks if user clicked on certain color selection slider
def click_check(x, hotbar_x, pos):
    if ((pygame.mouse.get_pos()[0] - hotbar_x//4*pos)**2 + (pygame.mouse.get_pos()[1]-(20+x))**2)**(1/2) <= 7:
        return True

#function sets new position for color selection slider
def x_set():
    if pygame.mouse.get_pos()[1]-20 >= 0 and pygame.mouse.get_pos()[1]-20 <= 255:
        return pygame.mouse.get_pos()[1]-20
    elif pygame.mouse.get_pos()[1]-20 < 0:
        return 0
    elif pygame.mouse.get_pos()[1]-20 > 255:
        return 255

screen.fill((255, 255, 255)) #fill screen with white color

#main loop
running = True
while running:
    #all events(keyboard and mouse)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #KEYDOWN events
            if event.key == pygame.K_ESCAPE: #stop main loop by ESCAPE(KEYDOWN)
                delfiles(1)
                running = False
            elif event.key == pygame.K_LCTRL: #make ctrl_k true by LCTRL(KEYDOWN)
                ctrl_k = True
            elif event.key == pygame.K_z: #make z_k true by 'z'(KEYDOWN)
                z_k = True
            elif event.key == pygame.K_y: #make y_k true by 'y'(KEYDOWN)
                y_k = True
        elif event.type == pygame.KEYUP: #KEYUP events
            if event.key == pygame.K_LCTRL: #make ctrl_k false by LCTRL(KEYUP)
                ctrl_k = False
            elif event.key == pygame.K_z: #make z_k false by 'z'(KEYUP)
                z_k = False
            elif event.key == pygame.K_y: #make y_k false by 'y'(KEYUP)
                y_k = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #MOUSEBUTTONDOWN events
            if event.button == 1:
                if pygame.mouse.get_pos()[0] > hotbar_x: #check if user cliked on board
                    #set mode based on tool number
                    if tool == 0 or tool == 1:
                        draw = True
                    else:
                        shapes_draw = True
                        shapes_initial_coor = pygame.mouse.get_pos()
                    screenshot(screenshot_number, screenshot_curr) #make screenshot
                else: #check if user cliked on hotbar
                    hotbar_click = True     
        elif event.type == pygame.MOUSEBUTTONUP: #MOUSEBUTTONUP events
            if event.button == 1:
                #turn all click variables into False if MOUSEBUTTONUP
                draw = False
                shapes_draw = False
                hotbar_click = False
                red_click = False
                green_click = False
                blue_click = False
                color_click = False
    
    #if tool is eraser set color to white, otherwise set it based on color positions
    if tool == 1:
        color = (255, 255, 255)
    else:
        color = (x_red, x_green, x_blue)

    #if user cliked LCTRL and 'z' in one time (Undo)
    if ctrl_k and z_k:
        if ctrl_z: #cheks if ctrl_z was pressed for the firs time, then make screenshot
            screenshot(screenshot_number, screenshot_curr)
            screenshot_curr-=1
            ctrl_z = False
        if screenshot_curr > 1: #check if current position of screenshot is more than 1, then blit screenshot
            image = pygame.image.load(os.path.join("screenshots", "screenshot" + str(screenshot_curr) + ".png"))
            screen.blit(image, (0, 0))
            screenshot_curr-=1
        z_k = False #set z_k to False

    #if user cliked LCTRL and 'y' in one time (Redo)
    if ctrl_k and y_k:
        if screenshot_curr < screenshot_number: #check if current position of screenshot is less or equal to total number of screenshots, then blit screenshot
            image = pygame.image.load(os.path.join("screenshots", "screenshot" + str(screenshot_curr+1) + ".png"))
            screen.blit(image, (0, 0))
            screenshot_curr+=1
        y_k = False #set y_k to False
    
    if hotbar_click: #check if user clicked at hotbar
        if not color_click:
            if not red_click: #check if user clicked at red color slider
                red_click = click_check(x_red, hotbar_x, 1)
            if not green_click: #check if user clicked at green color slider
                green_click = click_check(x_green, hotbar_x, 2)
            if not blue_click: #check if user clicked at blue color slider
                blue_click = click_check(x_blue, hotbar_x, 3)
            
            #check if user clicked at color selection button
            for i in range(0, len(color_buttons)):
                if pygame.mouse.get_pos()[0] >= hotbar_x//4*((i+3)%3+1)-10 and pygame.mouse.get_pos()[0] <= hotbar_x//4*((i+3)%3+1)+10 and pygame.mouse.get_pos()[1] >= 350 + 30*(i//3) and pygame.mouse.get_pos()[1] <= 350 + 30*(i//3) + 20:
                    x_red = color_buttons[i][0] 
                    x_green = color_buttons[i][1]
                    x_blue = color_buttons[i][2]
            
            #check if user cliked at size change button
            size_change_button_check(-1, 1, 575, hotbar_x)
            size_change_button_check(-5, 1, 600, hotbar_x)
            size_change_button_check(+1, 2, 575, hotbar_x)
            size_change_button_check(+5, 2, 600, hotbar_x)

            #check if user clicked at tool selection button
            for i in range(0, 8):
                if tool_button_check(i, hotbar_x):
                    tool = i

            color_click = True 

    #if user clicked at color slider, then set new position for color 
    if red_click:
        x_red = x_set()
    if green_click:
        x_green = x_set()
    if blue_click:
        x_blue = x_set()

    #check if user drawing shapes
    if shapes_draw: 
        #load last screenshot
        image = pygame.image.load(os.path.join("screenshots", "screenshot" + str(screenshot_curr) + ".png")) 
        screen.blit(image, (0, 0))

        if tool == 2: #if user have chosen 'circle' tool, then draw circle
            pygame.draw.circle(screen, color, shapes_initial_coor, ((shapes_initial_coor[0] - pygame.mouse.get_pos()[0])**2 + (shapes_initial_coor[1] - pygame.mouse.get_pos()[1])**2)**(1/2))
        elif tool == 3 or tool == 4: #if user have chosen 'rectangle' tool, then draw rectangle
            a_side = 0
            b_side = 0
            if tool == 3:
                a_side = abs(pygame.mouse.get_pos()[0]-shapes_initial_coor[0])
                b_side = abs(pygame.mouse.get_pos()[1]-shapes_initial_coor[1])
            elif tool == 4:
                a_side = max(abs(pygame.mouse.get_pos()[0]-shapes_initial_coor[0]), abs(pygame.mouse.get_pos()[1]-shapes_initial_coor[1]))
                b_side = a_side
            if pygame.mouse.get_pos()[0] >= shapes_initial_coor[0] and pygame.mouse.get_pos()[1] >= shapes_initial_coor[1]:
                pygame.draw.rect(screen, color, pygame.Rect(shapes_initial_coor[0], shapes_initial_coor[1], a_side, b_side))
            elif pygame.mouse.get_pos()[0] <= shapes_initial_coor[0] and pygame.mouse.get_pos()[1] >= shapes_initial_coor[1] and tool == 3:
                pygame.draw.rect(screen, color, pygame.Rect(pygame.mouse.get_pos()[0], shapes_initial_coor[1], a_side, b_side))
            elif pygame.mouse.get_pos()[0] <= shapes_initial_coor[0] and pygame.mouse.get_pos()[1] <= shapes_initial_coor[1]  and tool == 3:
                pygame.draw.rect(screen, color, pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], a_side, b_side))
            elif pygame.mouse.get_pos()[0] >= shapes_initial_coor[0] and pygame.mouse.get_pos()[1] <= shapes_initial_coor[1]  and tool == 3:
                pygame.draw.rect(screen, color, pygame.Rect(shapes_initial_coor[0], pygame.mouse.get_pos()[1], a_side, b_side))
        elif tool == 5:
            pygame.draw.polygon(screen, color, [shapes_initial_coor, pygame.mouse.get_pos(), (shapes_initial_coor[0], pygame.mouse.get_pos()[1])], 0)
        elif tool == 6:
            if shapes_initial_coor[1] < pygame.mouse.get_pos()[1]:
                pygame.draw.polygon(screen, color, [shapes_initial_coor, (pygame.mouse.get_pos()[0], shapes_initial_coor[1]), (0.5*(shapes_initial_coor[0] + pygame.mouse.get_pos()[0]), shapes_initial_coor[1] + abs(pygame.mouse.get_pos()[0] - shapes_initial_coor[0])*(3**(1/2))/2)], 0)
            else:
                pygame.draw.polygon(screen, color, [shapes_initial_coor, (pygame.mouse.get_pos()[0], shapes_initial_coor[1]), (0.5*(shapes_initial_coor[0] + pygame.mouse.get_pos()[0]), shapes_initial_coor[1] - abs(pygame.mouse.get_pos()[0] - shapes_initial_coor[0])*(3**(1/2))/2)], 0)
    if draw: #if user have chosen 'draw' tool, then draw
        current_coor = pygame.mouse.get_pos() #set new position for current_coor
        if current_coor == prev_сoor: #if current position if equal to previous, then draw circle in this coordinates
            pygame.draw.circle(screen, color, current_coor, radius)
        else: #else draw line by circles between previous and current positions 
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
    prev_сoor = pygame.mouse.get_pos() #set previous coordinate as current
    
    #draw all elements of hotbar
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 0, hotbar_x, yy)) #draw hotbar rectangle

    #draw red scale
    screen.blit(red_scale, red_scale_rect)
    pygame.draw.circle(screen, (140, 140, 140), (hotbar_x//4, 20+x_red), 12)
    pygame.draw.circle(screen, (x_red, 0, 0), (hotbar_x//4, 20+x_red), 10)

    #draw green scale
    screen.blit(green_scale, green_scale_rect)
    pygame.draw.circle(screen, (140, 140, 140), (hotbar_x//4*2, 20+x_green), 12)
    pygame.draw.circle(screen, (0, x_green, 0), (hotbar_x//4*2, 20+x_green), 10)

    #draw blue scale
    screen.blit(blue_scale, blue_scale_rect)
    pygame.draw.circle(screen, (140, 140, 140), (hotbar_x//4*3, 20+x_blue), 12)
    pygame.draw.circle(screen, (0, 0, x_blue), (hotbar_x//4*3, 20+x_blue), 10)

    pygame.draw.rect(screen, color, pygame.Rect(hotbar_x//2-20, 300, 40, 40)) #draw square, that indicates current color

    #draw all color change buttons 
    for i in range(0, len(color_buttons)): 
        pygame.draw.rect(screen, color_buttons[i], pygame.Rect(hotbar_x//4*((i+3)%3+1)-10, 350 + 30*(i//3), 20, 20)) 

    #draw text that indicates current value of size
    size_text = font.render("SIZE: " + str(radius), True, (50, 50, 50))
    size_text_rec = size_text.get_rect(topleft = (hotbar_x//2 - size_text.get_size()[0]//2, 555))
    screen.blit(size_text, size_text_rec)
    
    #draw all size change buttons
    size_change_button("-1", 1, 575, hotbar_x, font)
    size_change_button("-5", 1, 600, hotbar_x, font)
    size_change_button("+1", 2, 575, hotbar_x, font)
    size_change_button("+5", 2, 600, hotbar_x, font)

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(hotbar_x//3*(tool%2 + 1) - 18, 647 + (tool//2)*45, 36, 36)) #draw red square, that indicates current tool

    #draw all tools 
    screen.blit(tassel, tassel_rect)
    screen.blit(eraser, eraser_rect)
    screen.blit(circle_0, circle_0_rect)
    screen.blit(rectangle_0, rectangle_0_rect)
    screen.blit(square_0, square_0_rect)
    screen.blit(right_triangle, right_triangle_rect)
    screen.blit(equilateral_triangle, equilateral_triangle_rect)

    pygame.display.flip() #update screen

    pygame.time.wait(10) #wait for 10ms

