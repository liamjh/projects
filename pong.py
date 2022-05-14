import pygame, sys, os
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

VEL = 1



BAT = pygame.Rect(45, 415, 18, 130)
BAT2 = pygame.Rect(1219, 415, 18, 130)
BLOCK = pygame.Rect(624, 5, 16, 16)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)


def bat_movement(keyspressed, BAT):
    if keyspressed[pygame.K_w] and BAT.y - VEL > 10:
        BAT.y -= VEL
    elif keyspressed[pygame.K_s] and BAT.y + VEL < 820:
        BAT.y += VEL

def bat2_movement(keyspressed, BAT2):
    if keyspressed[pygame.K_UP] and BAT2.y - VEL > 10:
        BAT2.y -= VEL
    elif keyspressed[pygame.K_DOWN] and BAT2.y + VEL < 820:
        BAT2.y += VEL

def draw_window():
    x = 5
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, BAT)
    pygame.draw.rect(screen, WHITE, BAT2)
    pygame.draw.ellipse(screen, WHITE, ball)
    for i in range(24):
        pygame.draw.rect(screen, WHITE, [632, x, 16, 16])
        x = x + 40
    
  

    pygame.display.update()
while True: # mainloop
    for event in pygame.event.get():
        clock.tick(60)
        if event.type == pygame.QUIT:
             pygame.quit()
               

    ball_speed_x = 2
    ball_speed_y = 2
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height -10:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width -10:
        ball_speed_x *= -1
    
        
        
        


        





