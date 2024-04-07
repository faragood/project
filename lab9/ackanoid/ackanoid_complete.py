import pygame 
import random
from random import randint
pygame.init()

W, H = 1200, 800
FPS = 60
time_buff = 7
time_till_max_diff = 150
paddleW = 150
min_paddleW = 75
paddleSpeed = 20
ballRadius = 20
ballSpeed = 6    
max_ballSpeed = 10

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

def loss(W, H, FPS, screen, time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed):
    losefont = pygame.font.SysFont('comicsansms', 40)
    losetext = losefont.render('SPACE to restart', True, (255, 255, 255))
    losetextRect = losetext.get_rect()
    losetextRect.center = (W // 2, H // 2)
    screen.fill((0, 0, 0))
    screen.blit(losetext, losetextRect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game(W, H, FPS, screen, time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed)
        pygame.time.wait(1000//FPS)

def pause(W, H, FPS, screen, time_buff1, time_till_max_diff1, paddleW1, min_paddleW1, paddleSpeed1, ballRadius1, ballSpeed1, max_ballSpeed1, bg):
    global time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed
    time_buff0, time_till_max_diff0, paddleW0, min_paddleW0, paddleSpeed0, ballRadius0, ballSpeed0, max_ballSpeed0 = time_buff1, time_till_max_diff1, paddleW1, min_paddleW1, paddleSpeed1, ballRadius1, ballSpeed1, max_ballSpeed1
    font = pygame.font.SysFont('comicsansms', 50)
    pause_buttons_list = [['PAUSED', (255, 0, 0)], ['Continue', (255, 255, 255)], ['Start new game', (255, 255, 255)], ['Settings',(255, 255, 255)]]
    mode = "pause"
    action = ""
    click = False
    tick = 0
    while True:
        settings_buttons_list = [['SETTINGS', (255, 0, 0)], ['Time to maximum difficulty: ' + str(time_till_max_diff0) + 'sec', (255, 255, 255)], ['Time for buffs: ' + str(time_buff0) + 'sec', (255, 255, 255)], ['Initial width of paddle: ' + str(paddleW0),(255, 255, 255)], ['Minimum width of paddle: ' + str(min_paddleW0),(255, 255, 255)], ['Speed of paddle: ' + str(paddleSpeed0), (255, 255, 255)], ['Radius of the ball: ' + str(ballRadius0), (255, 255, 255)], ['Initial speed of ball: ' + str(ballSpeed0), (255, 255, 255)], ['Maximal speed of ball: ' + str(max_ballSpeed0), (255, 255, 255)], ['Save and start new game', (255, 0, 0)], ['Back', (255, 0, 0)]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if not click:
                        tick = 10
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        buttons_list = pause_buttons_list
        if mode != "pause":
            buttons_list = settings_buttons_list
        
        if click == True:
            if mode == "pause":
                for i in range(1, len(buttons_list)):
                    text = font.render(buttons_list[i][0], True, buttons_list[i][1])
                    text_rect = text.get_rect()
                    if pygame.mouse.get_pos()[0] >= W//2 - text_rect.width//2 and pygame.mouse.get_pos()[0] <= W//2 + text_rect.width//2 and pygame.mouse.get_pos()[1] >= H//3.5 + i*100 - text_rect.height//2 and pygame.mouse.get_pos()[1] <= H//3.5 + i*100 + text_rect.height//2:
                        action = "0-" + str(i)
            else:
                for i in range(1, len(buttons_list)):
                    save_text = font.render(buttons_list[len(buttons_list)-2][0], True, (255, 255, 255))
                    save_text_rect = save_text.get_rect()
                    back_text = font.render(buttons_list[len(buttons_list)-1][0], True, (255, 255, 255))
                    back_text_rect = back_text.get_rect()
                    add_text = font.render('+1', True, (255, 255, 255))
                    add_text_rect = add_text.get_rect()
                    drop_text = font.render('-1', True, (255, 255, 255))
                    drop_text_rect = drop_text.get_rect()
                    if pygame.mouse.get_pos()[1] >= 120 + i*60 - add_text_rect.height//2 and pygame.mouse.get_pos()[1] <= 80 + i*60 + add_text_rect.height//2:
                        if pygame.mouse.get_pos()[0] >= W - 150 - add_text_rect.width//2 and pygame.mouse.get_pos()[0] <= W - 150 + add_text_rect.width//2:
                            action = "1-" + str(i) + "-0"
                        elif pygame.mouse.get_pos()[0] >= W - 50 - drop_text_rect.width//2 and pygame.mouse.get_pos()[0] <= W - 50 + drop_text_rect.width//2:
                            action = "1-" + str(i) + "-1"
                        elif pygame.mouse.get_pos()[0] >= 50 and pygame.mouse.get_pos()[0] <= 50 + save_text_rect.width:
                            action = "1-" + str(i)
                        elif pygame.mouse.get_pos()[0] >= 50 and pygame.mouse.get_pos()[0] <= 50 + back_text_rect.width:
                            action = "1-" + str(i)
        
        if action:
            if tick >= 5:
                if action == "0-1":
                    return
                elif action == "0-2":
                    game(W, H, FPS, screen, time_buff1, time_till_max_diff1, paddleW1, min_paddleW1, paddleSpeed1, ballRadius1, ballSpeed1, max_ballSpeed1)
                elif action == "0-3":
                    mode = "settings"
                elif action == "1-1-0":
                    time_till_max_diff0+=1
                elif action == "1-1-1" and time_till_max_diff0-1 >= 1:
                    time_till_max_diff0-=1
                elif action == "1-2-0":
                    time_buff0+=1
                elif action == "1-2-1" and time_buff0-1 >= 1:
                    time_buff0-=1
                elif action == "1-3-0":
                    paddleW0+=1
                elif action == "1-3-1" and paddleW0-1 >= 1 and paddleW0-1 >= min_paddleW0:
                    paddleW0-=1
                elif action == "1-4-0" and min_paddleW0+1 <= paddleW0:
                    min_paddleW0+=1
                elif action == "1-4-1" and min_paddleW0-1 >= 1:
                    min_paddleW0-=1
                elif action == "1-5-0":
                    paddleSpeed0+=1
                elif action == "1-5-1" and paddleSpeed0-1 >= 1:
                    paddleSpeed0-=1
                elif action == "1-6-0":
                    ballRadius0+=1
                elif action == "1-6-1" and ballRadius0-1 >= 1:
                    ballRadius0-=1
                elif action == "1-7-0" and ballSpeed0+1 <= max_ballSpeed0:
                    ballSpeed0+=1
                elif action == "1-7-1" and ballSpeed0-1 >= 1:
                    ballSpeed0-=1
                elif action == "1-8-0":
                    max_ballSpeed0+=1
                elif action == "1-8-1" and max_ballSpeed0-1 >= 1 and ballSpeed0 <= max_ballSpeed0-1:
                    max_ballSpeed0-=1
                elif action == "1-9":
                    time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed = time_buff0, time_till_max_diff0, paddleW0, min_paddleW0, paddleSpeed0, ballRadius0, ballSpeed0, max_ballSpeed0
                    game(W, H, FPS, screen, time_buff0, time_till_max_diff0, paddleW0, min_paddleW0, paddleSpeed0, ballRadius0, ballSpeed0, max_ballSpeed0)
                elif action == "1-10":
                    time_buff0, time_till_max_diff0, paddleW0, min_paddleW0, paddleSpeed0, ballRadius0, ballSpeed0, max_ballSpeed0 = time_buff1, time_till_max_diff1, paddleW1, min_paddleW1, paddleSpeed1, ballRadius1, ballSpeed1, max_ballSpeed1
                    mode = "pause"
                action = ""
                tick = 0
            else:
                tick+=1

        screen.fill(bg)
        for i in range(len(buttons_list)):
            add_text = font.render('+1', True, (255, 255, 255))
            add_text_rect = add_text.get_rect()
            drop_text = font.render('-1', True, (255, 255, 255))
            drop_text_rect = drop_text.get_rect()
            text = font.render(buttons_list[i][0], True, buttons_list[i][1])
            text_rect = text.get_rect()
            if mode != "pause":
                text_rect.center = (50 + text_rect.width//2, 100 + i*60)
                if i != 0 and i != len(settings_buttons_list) - 1 and i != len(settings_buttons_list) - 2:
                    add_text_rect.center = (W - 150, 100 + i*60)
                    drop_text_rect.center = (W - 50, 100 + i*60)
                    screen.blit(add_text, add_text_rect)
                    screen.blit(drop_text, drop_text_rect)
            else:
                text_rect.center = (W//2 , H//3.5 + i*100)
            screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000//FPS)

def game(W, H, FPS, screen, time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed):
    clock = pygame.time.Clock()
    done = False
    bg = (0, 0, 0)

    #paddle
    paddleW0 = paddleW
    paddleH = 25
    paddle = pygame.Rect(W // 2 - paddleW0 // 2, H - paddleH - 30, paddleW0, paddleH)


    #Ball
    ballSpeed0 = ballSpeed
    ballRadius0 = ballRadius
    ball_rect = int(ballRadius0 * 2 ** 0.5)
    ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
    dx, dy = 1, -1

    ballSpeed_coef = (max_ballSpeed - ballSpeed0)/(time_till_max_diff*FPS)
    paddleW_coef = (paddleW0 - min_paddleW)/(time_till_max_diff*FPS)

    time_buff_1 = 0
    time_buff_2 = 0
    time_buff_3 = 0
    time_buff_coef = time_buff/(time_buff*FPS)

    #Game score
    game_score = 0
    game_score_fonts = pygame.font.SysFont('comicsansms', 40)
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
    game_score_rect = game_score_text.get_rect()
    game_score_rect.center = (210, 20)

    #Catching sound
    collision_sound = pygame.mixer.Sound('audio/catch.mp3')

    def detect_collision(dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        if delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy


    #block settings
    block_list = [[randint(1, 20), pygame.Rect(10 + 120 * i, 50 + 70 * j,
            100, 50)] for i in range(10) for j in range (4)]
    color_list = [(random.randrange(200, 255), 
        random.randrange(200, 255),  random.randrange(200, 255))
                for i in range(10) for j in range(4)] 
    #print(block_list)
    #Game over Screen
    losefont = pygame.font.SysFont('comicsansms', 40)
    losetext = losefont.render('Game Over', True, (255, 255, 255))
    losetextRect = losetext.get_rect()
    losetextRect.center = (W // 2, H // 2)

    #Win Screen
    winfont = pygame.font.SysFont('comicsansms', 40)
    wintext = losefont.render('You win yay', True, (0, 0, 0))
    wintextRect = wintext.get_rect()
    wintextRect.center = (W // 2, H // 2)


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause(W, H, FPS, screen, time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed, bg)

        screen.fill(bg)
        
        # print(next(enumerate(block_list)))
        for i in range(len(block_list)):
            if block_list[i][0] >= 1 and block_list[i][0] <= 3:
                pygame.draw.rect(screen, (30, 30, 30), block_list[i][1])
            elif block_list[i][0] == 4:
                pygame.draw.rect(screen, (255, 0, 0), block_list[i][1])
            elif block_list[i][0] == 5:
                pygame.draw.rect(screen, (0, 255, 0), block_list[i][1])
            elif block_list[i][0] == 6:
                pygame.draw.rect(screen, (0, 0, 255), block_list[i][1])
            else:
                pygame.draw.rect(screen, color_list[i], block_list[i][1])
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius0)
        # print(next(enumerate (block_list)))

        if paddleW0 > min_paddleW:
            paddleW0-=paddleW_coef
        else:
            paddleW0 = min_paddleW
        paddle.width = paddleW0
        if time_buff_3 != 0:
            paddle.width = 300
        if ballSpeed0 < max_ballSpeed:
            ballSpeed0+=ballSpeed_coef
        else:
            ballSpeed0 = max_ballSpeed
        if time_buff_1 != 0:
            ballRadius0 = 100
        else:
            ballRadius0 = ballRadius
        ball_rect = int(ballRadius * 2 ** 0.5)
        ball.width = ball_rect
        ball.height = ball_rect

        #Ball movement
        ball.x += ballSpeed0 * dx
        ball.y += ballSpeed0 * dy

        #Collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        #Collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        #Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        #Collision blocks
        hitIndex = ball.collidelist([i[1] for i in block_list])

        if hitIndex != -1:
            hitRect = block_list[hitIndex][1]
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            if block_list[hitIndex][0] >= 1 and block_list[hitIndex][0] <= 3 and time_buff_2 == 0:
                None
            else:
                if block_list[hitIndex][0] == 4:
                    time_buff_1 = time_buff
                if block_list[hitIndex][0] == 5:
                    time_buff_2 = time_buff
                if block_list[hitIndex][0] == 6:
                    time_buff_3 = time_buff
                block_list.pop(hitIndex)
                hitColor = color_list.pop(hitIndex)
                game_score += 1
                collision_sound.play()
        #Game score
        time_buff_1_text = ""
        if time_buff_1 > 0:
            time_buff_1_text = "Big ball: " + str(round(time_buff_1)) + " "
            time_buff_1 -= time_buff_coef
        else:
            time_buff_1 = 0
        time_buff_2_text = ""
        if time_buff_2 > 0:
            time_buff_2_text = "Break unbreakable: " + str(round(time_buff_2)) + " "
            time_buff_2 -= time_buff_coef
        else:
            time_buff_2 = 0
        time_buff_3_text = ""
        if time_buff_3 > 0:
            time_buff_3_text = "Big paddle: " + str(round(time_buff_3)) + " "
            time_buff_3 -= time_buff_coef
        else:
            time_buff_3 = 0
        game_score_text = game_score_fonts.render(f"Your game score is: {game_score} " + time_buff_1_text + time_buff_2_text + time_buff_3_text, True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        #Win/lose screens
        if ball.bottom > H:
            loss(W, H, FPS, screen, time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed)
        elif not len(block_list):
            screen.fill((255,255, 255))
            screen.blit(wintext, wintextRect)
        # print(pygame.K_LEFT)
        #Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed


        pygame.display.flip()
        pygame.time.wait(1000//FPS)
game(W, H, FPS, screen, time_buff, time_till_max_diff, paddleW, min_paddleW, paddleSpeed, ballRadius, ballSpeed, max_ballSpeed)