from curses.textpad import rectangle
import pygame
from pygame.draw import *

pygame.init()

FPS = 30

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH = 400
HEIGHT = 400

RADIUS = min(WIDTH, HEIGHT)//6

screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle(screen, BLACK, (WIDTH//2, HEIGHT//2), (RADIUS * 11)//10)
circle(screen, YELLOW, (WIDTH//2, HEIGHT//2), RADIUS)

rect(screen, BLACK, (WIDTH//2-RADIUS//2, HEIGHT//2+RADIUS//2, RADIUS, RADIUS//7))

circle(screen, BLACK, (WIDTH//2+RADIUS//3, HEIGHT//2-RADIUS//3), RADIUS//5)
circle(screen, RED, (WIDTH//2+RADIUS//3, HEIGHT//2-RADIUS//3), RADIUS//6)
circle(screen, BLACK, (WIDTH//2+RADIUS//3, HEIGHT//2-RADIUS//3), RADIUS//10)

circle(screen, BLACK, (WIDTH//2-RADIUS//3-RADIUS//10, HEIGHT//2-RADIUS//3+RADIUS//20), RADIUS//4)
circle(screen, RED, (WIDTH//2-RADIUS//3-RADIUS//10, HEIGHT//2-RADIUS//3+RADIUS//20), RADIUS//5)
circle(screen, BLACK, (WIDTH//2-RADIUS//3-RADIUS//10, HEIGHT//2-RADIUS//3+RADIUS//20), RADIUS//10)

polygon(screen, BLACK, [(WIDTH//2+RADIUS//6, HEIGHT//2-RADIUS//3-RADIUS//4), (WIDTH//2+RADIUS, HEIGHT//2-RADIUS)], RADIUS//10)
polygon(screen, BLACK, [(WIDTH//2-RADIUS//3-RADIUS//10+RADIUS//6, HEIGHT//2-RADIUS//3+RADIUS//20-RADIUS//4), (WIDTH//2-RADIUS//3-RADIUS//10-RADIUS, HEIGHT//2-RADIUS//3+RADIUS//20-RADIUS)], RADIUS//10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
