import sys
import pygame
from random import randint

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (32, 52, 71)

pygame.init()
GAME_FONT = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Awesom shooter game')

FIGHTER_STEP = 5
FIGHTER_IMAGE = pygame.image.load('images/fighter.png')
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
fighter_x, fighter_y = SCREEN_WIDTH / 2 - FIGHTER_WIDTH / 2, SCREEN_HEIGHT - FIGHTER_HEIGHT
fighter_is_moving_left, fighter_is_moving_right = False, False

BALL_STEP = 3
BALL_IMAGE = pygame.image.load('images/ball.png')
BALL_WIDTH, BALL_HEIGHT = BALL_IMAGE.get_size()
ball_x, ball_y = 0, 0
is_ball_was_fired = False

ALIEN_STEP = 1
alien_speed = ALIEN_STEP
ALIEN_IMAGE = pygame.image.load('images/alien.png')
ALIEN_WIDTH, ALIEN_HEIGHT = ALIEN_IMAGE.get_size()
alien_x, alien_y = randint(0, SCREEN_WIDTH - ALIEN_WIDTH), 0
is_alien_was_fired = False

is_running_game = True

while is_running_game:
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

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x < SCREEN_WIDTH - FIGHTER_WIDTH:
        fighter_x += FIGHTER_STEP

    alien_y += alien_speed

    if is_ball_was_fired and ball_y + BALL_HEIGHT < 0:
        is_ball_was_fired = False

    if is_ball_was_fired:
        ball_y -= BALL_STEP

    screen.fill(SCREEN_COLOR)
    screen.blit(FIGHTER_IMAGE, (fighter_x, fighter_y))
    screen.blit(ALIEN_IMAGE, (alien_x, alien_y))

    if is_ball_was_fired:
        screen.blit(BALL_IMAGE, (ball_x, ball_y))

    pygame.display.update()

    if alien_y + ALIEN_HEIGHT > fighter_y:
        is_running_game = False

    if (is_ball_was_fired and
            alien_x < ball_x < alien_x + ALIEN_WIDTH - BALL_WIDTH and
            alien_y < ball_y < alien_y + ALIEN_HEIGHT - BALL_HEIGHT):
        is_ball_was_fired = False
        alien_x, alien_y = randint(0, SCREEN_WIDTH - ALIEN_WIDTH), 0
        alien_speed += ALIEN_STEP / 2

game_over_text = GAME_FONT.render('Game over', True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()
