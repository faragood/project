import pygame 
import random
from random import randint
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
min_paddleW = 75
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
max_ballSpeed = 10
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

time_till_max_diff = 150
ballSpeed_coef = (max_ballSpeed - ballSpeed)/(time_till_max_diff*FPS)
paddleW_coef = (paddleW - min_paddleW)/(time_till_max_diff*FPS)

time_buff = 7
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
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

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
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    if paddleW > min_paddleW:
        paddleW-=paddleW_coef
    else:
        paddleW = min_paddleW
    paddle.width = paddleW
    if time_buff_3 != 0:
        paddle.width = 300
    if ballSpeed < max_ballSpeed:
        ballSpeed+=ballSpeed_coef
    else:
        ballSpeed = max_ballSpeed
    if time_buff_1 != 0:
        ballRadius = 100
    else:
        ballRadius = 20
    ball_rect = int(ballRadius * 2 ** 0.5)
    ball.width = ball_rect
    ball.height = ball_rect

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

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
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
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