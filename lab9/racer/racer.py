#import all libraries and init them
import pygame, sys
from pygame.locals import *
from random import randint
pygame.init()

#initial variables
roads = 7 #number of roads
xx = roads*105 #width of screen based on number of roads
yy = 750 #length of screen
font = pygame.font.Font(None, 100) #font for all text
screen = pygame.display.set_mode((xx, yy)) #set screen

#set name of screen
pygame.display.set_caption("Racer")

#function for loss
def loss(xx, yy, font, roads):
    #display text "You lose!" and "SPACE to restart" 
    font = pygame.font.Font(None, 70) #set font
    text = font.render("You lose!", True, (0, 180, 0)) #"You lose!"
    text_rec = text.get_rect(topleft = (xx//2 - text.get_size()[0]//2, yy//2 - text.get_size()[1]//2)) #set location for "You lose!"
    screen.blit(text, text_rec) #blit text
    text = font.render("(SPACE to restart)", True, (0, 180, 0)) #"SPACE to restart"
    text_rec = text.get_rect(topleft = (xx//2 - text.get_size()[0]//2, yy//1.8 - text.get_size()[1]//2)) #set location for "SPACE to restart"
    screen.blit(text, text_rec) #blit text
    pygame.display.update() #update screen

    #wait until player will quit the game or will press 'ESCAPE' for quit game or 'SPACE' to start new game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() #quit the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game(xx, yy, font, roads) #start new game
                elif event.key == pygame.K_ESCAPE:
                    exit() #quit the game
        pygame.time.delay(50) #wait for 50ms

#funtion for game   
def game(xx, yy, font, roads):
    player_car0 = pygame.image.load("images/player_car.png") #load player car
    player_car0 = pygame.transform.scale(player_car0, (player_car0.get_size()[0]//4, player_car0.get_size()[1]//4)) #set size for player car

    enemy_car = pygame.image.load("images/enemy_car.png") #load enemy car 
    enemy_car = pygame.transform.scale(enemy_car, (75, 75/enemy_car.get_size()[0]*enemy_car.get_size()[1])) #set size for enemy car

    coin = pygame.image.load("images/coin1.png") #load coin 
    coin = pygame.transform.scale(coin, (90, 72)) #set size for coin

    little_coin = pygame.transform.scale(coin, (coin.get_size()[0]//2, coin.get_size()[1]//2)) #load little coin
    little_coin_rect = little_coin.get_rect(topleft = (xx-100, 0)) #set sixe for little coin

    #function for adding enemies    
    def random_enemy(roads, appear_time0, appear_rand_time_range, enemies):
        rand_road = randint(1, roads) #random road for enemy
        appear_time = appear_time0 + randint(0, int(appear_rand_time_range)) #random time for appearing new enemy
        return (rand_road, appear_time) #return variables

    #funtion for adding coins 
    def random_coin(road):
        rand_road = randint(1, road) #random road for coin
        return rand_road #return variables
    
    #function for displaying road stripes
    def stripes(x_stripes, roads):
        x1_stripes = 0 #variavble of coordinates for stripe lines(x coordnates)
        #loop for drawing columns of stripes
        for i in range(1, roads):
            x1_stripes+=xx//roads #add certain coordinate for new line of stripes 
            j = x_stripes #bias for stripes(y coordinate)
            #loop for drawing raws of stripes until it won't be greater than yy
            while j <= yy:
                pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(x1_stripes, j, 8, 50)) #draw rectangle
                j+=100 #add 100 to j for drawing new stripe

    #function for displaying player car
    def blit_player_car(x, ac):
        player_car = pygame.transform.rotate(player_car0, -ac*2) #turn player car for specific angle based on its acceleration
        player_car_rect = player_car.get_rect(topleft = (x, yy/1.1 - player_car.get_size()[1])) #set new position based on x coordinate
        screen.blit(player_car, player_car_rect) #blit player car

    #function for displaying all enemies
    def blit_enemies_cars(enemies):
        #loop for displaying all enemies
        for i in enemies:
            enemy_car_rect = enemy_car.get_rect(topleft = (xx//(roads)*i[0] - enemy_car.get_size()[0] - 10, i[1])) #set new position for enemy
            screen.blit(enemy_car, enemy_car_rect) #blit enemy car
    
    #----------------------CHANGED----------------------
    #function for displaying all coins
    def blit_coins(coins):
        #loop for displaying all coins
        for i in coins:
            color = (0, 0, 0)
            if i[1] == 1:
                color = (255, 215, 0)
            elif i[1] == 3:
                color = (150, 200, 225)
            else:
                color = (0, 201, 87)
            pygame.draw.circle(screen, color, (xx//(roads)*i[0] - 5 - 40, i[2]+30), 30)#blit coin
            pygame.draw.circle(screen, (255, 255, 255), (xx//(roads)*i[0] - 5 - 40, i[2]+30), 20) #blit coin's inner side
    #---------------------------------------------------

    #all variables
    fps = 60 #fps (frames per second)
    tick = 100//fps #variable for waiting to draw next frame
    enemy_tick = 0 #varialbe for waiting to add new enemy
    appear_time0 = 200 #iunitial time for appering enemy
    appear_rand_time_range = 600 #random range of time of appearing enemy
    min_appear_rand_time_range = 200 #minimum range of time of appearing enemy
    appear_time = 1000 #time of appering enemy (appear_time = appear_time0 + [random value from 0 to appear_rand_time_range])
    tick_0 = 0 #variable for waiting to draw next frame
    speed = 7.5 #speed of enemies
    max_speed = 14 #maximal speed
    x = xx//2 - player_car0.get_size()[0]//2 #cooridinate of player car(initially in the center of the screen)
    x_stripes = -50 #y coordinates for stripes
    ac = 0 #acceleration of player car
    enemies = [] #list of enemies [[road, (y coordinate)], ...]
    right_move = False #variable checks if player moving to right
    left_move = False #variable checks if player moving to left
    coin_score = 0 #coin score of player
    coin_appear = 10 #variable to set frequency appearing coins instead of enemy(the lower, the more often)

    #----------------------CHANGED----------------------
    catch_sound = pygame.mixer.Sound("sound/catch.mp3") #coin catch sound
    background_music = pygame.mixer.Sound("sound/background_music.mp3") #background music
    crash = pygame.mixer.Sound("sound/crash.mp3") #crash sound
    coins = [] #list of coins [[road, weigth of the coin, (y coordinate)], ...]
    valuable_coins_appear_chance = 20 #variable to regulate the chance of appearing valuable coins(3 and 5 weigth coins) (then higher, then chance less)
    coin_speed_increase0 = 3 #number of coins coins that need to increase speed
    coin_speed_increase = 0 #variable to check how many coins player has collected from previous speed increase
    coin_until_max_dif = 150#coins until game will reach maximum difficulty (100 coins)
    speed_coef = (max_speed - speed)/(coin_until_max_dif//coin_speed_increase0) #variable for adding to speed based on time_until_max_dif
    appear_rand_time_range_coef = (appear_rand_time_range - min_appear_rand_time_range)/(coin_until_max_dif//coin_speed_increase0) #variable for taking away from appear_rand_time_range based on time_until_max_dif
    
    pygame.mixer.stop() #stop all sounds 
    background_music.play(-1) #play backgound music
    #---------------------------------------------------
    
    #main game loop
    gameOn = True
    while gameOn:

        #loop for checking for keyboard events
        for event in pygame.event.get():
            #quit the game 
            if event.type == pygame.QUIT:
                exit()
            #check for KEYDOWN events
            elif event.type == pygame.KEYDOWN:
                #start to move player car right if 'RIGHT' or 'd' was pressed down
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right_move = True
                #start to move player car left if 'LEFT' or 'a' was pressed
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left_move = True
                #quit the game 
                elif event.key == pygame.K_ESCAPE:
                    exit()
            #check for KEYUP events
            elif event.type == pygame.KEYUP:
                #stop to move player car right if 'RIGHT' or 'd' was pressed up
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right_move = False
                #stop to move player car left if 'LEFT' or 'a' was pressed up
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left_move = False
                    
        #check if right_move if True, then increase acceleration
        if right_move == True:
            if ac < 10:
                ac+=1
            else:
                ac = 10
        #check if left_move if True, then decrease acceleration
        elif left_move == True:
            if ac > -10:
                ac-=1
            else:
                ac = -10
        #if right_move and left_move are both False, then start to reduce acceleration
        elif left_move == False and right_move == False:
            ac*=0.8
        
        x += ac*1 #add acceleration to player car coordinates

        #check for so that player does not go beyond screen
        if x >= xx - player_car0.get_size()[0]:
            x = xx - player_car0.get_size()[0]
            ac*=0.5 #start to reduce acceleration if player car touches border
        elif x <= 0:
            x = 0
            ac*=0.5 #start to reduce acceleration if player car touches border
            
        #move stripes based on (speed - 3)
        if x_stripes <= 50:
            x_stripes+=(speed-3)
        else:
            x_stripes = -50
        
        #move all enemies based on speed
        for i in range(len(enemies)-1):
            if enemies[i][1] <= yy:
                enemies[i][1]+=speed
            else:
                del enemies[i]

        #move coins based on (speed - 3) 
        for i in range(len(coins)-1):
            if coins[i][2] <= yy:
                coins[i][2]+=(speed-3)
            else:
                del coins[i]
        
        #check if player touched enemy car
        for i in enemies:
            if abs(x - (xx//(roads)*i[0] - enemy_car.get_size()[0] - 10)) < 60 and abs((i[1] + enemy_car.get_size()[1]//4) - (yy/1.1 - player_car0.get_size()[1])) < 100:
                #----------------------CHANGED----------------------
                background_music.stop() #stop background music
                crash.play() #play car crash sound
                #---------------------------------------------------
                loss(xx, yy, font, roads)#summon loss function 
        
        #----------------------CHANGED----------------------
        #check if player touched coin
        for i in range(len(coins)-1):
            if (((yy/1.1 - player_car0.get_size()[1]) - coins[i][2])**2 + ((xx//(roads)*coins[i][0] - coin.get_size()[0] - 5) - (x))**2)*(1/2) <= 50**2:
                coin_score+=coins[i][1] #add coin weigth to coin score
                catch_sound.play() #play catch sound
                del coins[i]
                #gradually increase speed till max_speed
                if coin_speed_increase == coin_speed_increase0:
                    if speed+speed_coef <= max_speed:
                        speed+=speed_coef
                    else:
                        speed = max_speed
            
                    #gradually decrese speed till min_appear_rand_time_range
                    if appear_rand_time_range-appear_rand_time_range_coef >= min_appear_rand_time_range:
                        appear_rand_time_range-=appear_rand_time_range_coef
                    else:
                        appear_rand_time_range = min_appear_rand_time_range
                    coin_speed_increase = 0
                else:
                    coin_speed_increase+=1
        #---------------------------------------------------

        #wait until enemy_tick will reach appear_time and then add new enemy or coin
        if enemy_tick >= appear_time:
            appear_time = random_enemy(roads, appear_time0, appear_rand_time_range,enemies)[1] #set new time for appear_time
            rando = randint(1,int(coin_appear)) #variable to randomize appearing enemy or coin
            if rando != 1: #in 1 out of [coin_appear] events there will appear coin instead of enemy
                enemies.append([random_enemy(roads, appear_time0, appear_rand_time_range, enemies)[0], -200]) #add new enemy
            else:
                #----------------------CHANGED----------------------
                random_coin_num = randint(1, valuable_coins_appear_chance)
                if random_coin_num == 1:
                    coins.append([random_coin(roads), 5, -200]) #add new coin (weight 5)
                elif random_coin_num >= 2 and random_coin_num <= 3:
                    coins.append([random_coin(roads), 3, -200]) #add new coin (weight 3)
                else:
                    coins.append([random_coin(roads), 1, -200]) #add new coin (weight 1)
                #---------------------------------------------------
            enemy_tick = 0 #set enemy tick to 0ms 
        else:
            enemy_tick+= 10 #add 10ms to enemy_tick
        
        #draw next frame
        if tick_0 >= tick:
            screen.fill((20, 20, 20)) #clean whole screen
            stripes(x_stripes, roads) #draw stripes
            blit_enemies_cars(enemies) #draw all enemies
            blit_coins(coins) #draw all coins
            font = pygame.font.Font(None, 50) #set font
            text = font.render(str(coin_score), True, (255, 255, 255)) #set text of coin scorer
            text_rec = text.get_rect(topleft = (xx-55   , little_coin.get_size()[1]//2-text.get_size()[1]//2)) #set position of the score text in the top right corner
            screen.blit(text, text_rec) #draw score
            screen.blit(little_coin, little_coin_rect) #draw little coin
            blit_player_car(x,ac) #draw player car
            pygame.display.update() #unpdate screen
            tick_0 = 0 #set tick_0 to 0ms
        else:
            tick_0+=1 #add 1ms to tick_0
            
        pygame.time.delay(10) #wait for 10ms 
        
game(xx, yy, font, roads) #start the game
