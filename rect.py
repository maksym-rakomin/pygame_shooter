import sys
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (49,183,255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My py game')

rect_width, rect_height = 100, 200
rect_x, rect_y = SCREEN_WIDTH / 2 - rect_width / 2, SCREEN_HEIGHT / 2 - rect_height / 2
rect_color = (223, 0, 44)

STEP = 10

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x < SCREEN_WIDTH - rect_width:
                rect_x += STEP
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y < SCREEN_HEIGHT - rect_height:
                rect_y += STEP

    screen.fill(SCREEN_COLOR)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()
