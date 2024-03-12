import sys
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (32, 52, 71)
STEP = 1

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Awesom shooter game')

FIGHTER_IMAGE = pygame.image.load('images/fighter.png')
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
fighter_x, fighter_y = SCREEN_WIDTH / 2 - FIGHTER_WIDTH / 2, SCREEN_HEIGHT - FIGHTER_HEIGHT
fighter_is_moving_left, fighter_is_moving_right = False, False

BALL_STEP = 1.5
BALL_IMAGE = pygame.image.load('images/ball.png')
BALL_WIDTH, BALL_HEIGHT = BALL_IMAGE.get_size()
ball_x, ball_y = 0, 0
is_ball_was_fired = False

ALIEN_STEP = 1
ALIEN_IMAGE = pygame.image.load('images/alien.png')
ALIEN_WIDTH, ALIEN_HEIGHT = ALIEN_IMAGE.get_size()
alien_x, alien_y = 0, 0
is_alien_was_fired = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True

            if event.key == pygame.K_SPACE:
                is_ball_was_fired = True
                ball_x, ball_y = fighter_x + FIGHTER_WIDTH / 2 - BALL_WIDTH / 2, fighter_y - BALL_HEIGHT

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= STEP:
        fighter_x -= STEP
    if fighter_is_moving_right and fighter_x < SCREEN_WIDTH - FIGHTER_WIDTH:
        fighter_x += STEP

    if is_ball_was_fired and ball_y + BALL_HEIGHT < 0:
        is_ball_was_fired = False

    if is_ball_was_fired:
        ball_y -= BALL_STEP

    screen.fill(SCREEN_COLOR)
    screen.blit(FIGHTER_IMAGE, (fighter_x, fighter_y))

    if is_ball_was_fired:
        screen.blit(BALL_IMAGE, (ball_x, ball_y))

    pygame.display.update()
