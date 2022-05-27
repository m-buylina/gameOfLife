from telnetlib import GA
import pygame
from pygame.locals import *
from sys import exit
import random

import game

SIZE = 500
GAP = 20
MARGIN = 40
FIELDS = int(SIZE / GAP)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SIZE, SIZE + MARGIN))
screen.fill((255, 255, 255))
pygame.display.set_caption('Game of life')

test_s = pygame.Surface((10, 10))
test_s.fill(color = 'Red')
test_font = pygame.font.SysFont('Arial', 22)



board = [[random.randint(0, 1) for i in range(FIELDS)] for j in range(FIELDS)]

game.print_board(board, 0)
age = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    #life
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item:
                x = GAP * j
                y = GAP * i + MARGIN
                pygame.draw.rect(screen, "Red", (x, y, GAP, GAP))

    board = game.next_state(board)

    #grid
    [pygame.draw.line(screen, 'Black', (x, MARGIN), (x, SIZE + MARGIN)) for x in range(GAP, SIZE, GAP)]
    [pygame.draw.line(screen, 'Black', (0, y + MARGIN), (SIZE, y + MARGIN)) for y in range(0, SIZE, GAP)]

    text_surface = test_font.render('Age: ' + str(age), True, 'Black')
    screen.blit(text_surface, (210, 10))



    age = age + 1
    pygame.display.flip()
    clock.tick(5)
