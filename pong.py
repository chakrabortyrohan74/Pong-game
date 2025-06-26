import pygame, sys, random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

title = pygame.display.set_caption('Pong Game')

text  = pygame.font.Font('freesansbold.ttf', size=20)

clock = pygame.time.Clock()

WHITE = (255,255,255)

mixer.music.load('game_music.mp3')
mixer.music.play(-1)

pong_music = mixer.Sound('pong.mp3')
game_over_music = mixer.Sound('game_over.mp3')

pong1_y = 250
pong2_y = 250

pong1_change = 0
pong2_change = 0

ball_X = 400
ball_y = 289
    
ball_velx = 5
ball_vely = 5

score1 = 0
score2 = 0

def drawElememts():
    pygame.draw.rect(screen, WHITE, (1,pong1_y,30,100))
    
    pygame.draw.rect(screen, WHITE, (769,pong2_y,30,100))
    
    pygame.draw.circle(screen, WHITE, (ball_X,ball_y),10)
    
    for i in range(0,600,30):
        pygame.draw.rect(screen, WHITE, (395,i,10,20))

def ballReset(x1,y1,x2,y2):
    global ball_X,ball_y
    ball_X = random.randint(x1,y1)
    ball_y = random.randint(x2,y2)

def isCollision():
    global ball_velx
    if ball_X <= 30:
        for coordinates1 in range(pong1_y,pong1_y+100):
            if coordinates1 == ball_y:
                ball_velx *= -1
                pong_music.play()
                
    global ball_vely
    if ball_X >= 770:
        for coordinates2 in range(pong2_y,pong2_y+100):
            if coordinates2 == ball_y:
                ball_velx *= -1
                pong_music.play()            

def isSCore():
    global score1, score2
    if ball_X < 0:
        score1 += 1
        game_over_music.play()
        # pygame.time.delay(60)
        # print("Score1 " + str(score1))
        ballReset(400,600,20,580)

    if ball_X > 800:
        score2 += 1 
        game_over_music.play()
        # pygame.time.delay(60)
        # print("Score2 " + str(score2))
        ballReset(200,400,20,580) 
        
    scoreboard1 = text.render("PLAYER1 : " + str(score2), True, WHITE)
    screen.blit(scoreboard1, (170,20))
    
    scoreboard2 = text.render("PLAYER2 : " + str(score1), True, WHITE)
    screen.blit(scoreboard2, (570,20))

while True:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()        
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pong1_change -= 5   
            if event.key == pygame.K_DOWN:
                pong1_change += 5
            if event.key == pygame.K_a:
                pong2_change -= 5
            if event.key == pygame.K_s:
                pong2_change += 5
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pong1_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_s:
                pong2_change = 0          
                
        
    pong1_y += pong1_change
    
    if pong1_y < 0:
        pong1_y = 0
    if pong1_y > 500:  
        pong1_y = 500
        
    pong2_y += pong2_change
    
    if pong2_y < 0:
        pong2_y = 0
    if pong2_y > 500:  
        pong2_y = 500    
    
    ball_X += ball_velx
    ball_y += ball_vely
    
    if ball_y > 590:
        ball_velx *= 1
        ball_vely *= -1
    
    if ball_y <= 10:
        ball_velx *= 1
        ball_vely *= -1           
    
    isCollision()
    
    isSCore()
        
    drawElememts()
    
    pygame.display.update() 
    clock.tick(60)       