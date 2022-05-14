import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500 # constant values
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #two variables, w and h for the window size of the game
pygame.display.set_caption('Game')

WHITE = (255, 255, 255) # RGB colour scheme
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

VEL = 5

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

BULLET_VEL = 7  

MAX_BULLETS = 5

FPS = 60 # how many times the game refreshes the run loop a second

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2 # to create our own user event 

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (900, 500))


HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')) # we take the scaled ship and rotate it
YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png')) # using os module to import assets
RED_SHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0,0)) # blit the image to the background
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render('Health: ' + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render('Health: ' + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    WIN.blit(YELLOW_SHIP, (yellow.x, yellow.y)) #blit is used to draw an image onto a surface, for text or 2d images
    WIN.blit(RED_SHIP, (red.x, red.y))


    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()
        
def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x -  VEL > 0:#left
        yellow.x -= VEL
    elif keys_pressed[pygame.K_s] and yellow.y + VEL < 445:#down
        yellow.y += VEL
    elif keys_pressed[pygame.K_d] and yellow.x + VEL < 405:#right
        yellow.x += VEL
    elif keys_pressed[pygame.K_w] and yellow.y - VEL > 0:#up
        yellow.y -= VEL

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > 455:#left
        red.x -= VEL
    elif keys_pressed[pygame.K_DOWN]and red.y + VEL < 445:#down
        red.y += VEL
    elif keys_pressed[pygame.K_RIGHT]and red.x + VEL < 860:#right
        red.x += VEL
    elif keys_pressed[pygame.K_UP]and red.y - VEL > 0:#up
        red.y -= VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > 900:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT)) # post out event so we can check of it
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
                
    
    


def main(): #main loop
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # we ned to define two 'boxes' to keep track of the spaceships x,y and height/width
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []

    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)     # this makes sure the while loop is refreshed every 60 times a second
        for event in pygame.event.get(): # gets/checks for events in the game
            if event.type == pygame.QUIT:
                run = False # end game if user quits the window
                pygame.quit()

            if event.type == pygame.KEYDOWN: # bullets work as so, we create a new rect at the x, y of the front of our ship, we then append to a list
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.height, yellow.y + yellow.width - 25, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.width - 25, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
                

            if event.type == YELLOW_HIT:
               yellow_health -= 1
               BULLET_HIT_SOUND.play()

        winner_text = ''
        if red_health <= 0:
            winner_text = 'dub for yellow'

        if yellow_health <= 0:
            winner_text = 'dub for red'

        if winner_text != '':
            draw_winner(winner_text)
            break
                    
                

        keys_pressed = pygame.key.get_pressed()# this will get the keys that are pressed every time the while loop executes, 60fps
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

      
    main()


if __name__ == '__main__': # makes sure the .py wont be loaded for any other reason than running the file directly 
    main()
            
