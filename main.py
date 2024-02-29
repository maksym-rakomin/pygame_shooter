import sys
import pygame


clock = pygame.time.Clock()

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My py game')


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 0, 0))
    pygame.display.update()

    clock.tick(1)

