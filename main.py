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

ROCKET_IMAGE = pygame.image.load('images/rocket.png')
ROCKET_WIDTH, ROCKET_HEIGHT = ROCKET_IMAGE.get_size()
rocket_x, rocket_y = fighter_x + FIGHTER_WIDTH / 2 - ROCKET_WIDTH / 2, fighter_y - ROCKET_HEIGHT
is_rocket_was_fired = False

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
                is_rocket_was_fired = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False
            #
            # if event.key == pygame.K_SPACE:
            #     is_rocket_was_fired = False

    if fighter_is_moving_left and fighter_x >= STEP:
        fighter_x -= STEP
    if fighter_is_moving_right and fighter_x < SCREEN_WIDTH - FIGHTER_WIDTH:
        fighter_x += STEP

    if is_rocket_was_fired and rocket_y < SCREEN_HEIGHT - fighter_y - FIGHTER_HEIGHT:
        rocket_y += 1

    screen.fill(SCREEN_COLOR)
    screen.blit(FIGHTER_IMAGE, (fighter_x, fighter_y))
    if is_rocket_was_fired:
        screen.blit(ROCKET_IMAGE, (rocket_x, rocket_y))

    pygame.display.update()
