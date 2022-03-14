# Libs
import os
import random
import time

import pygame
from pygame.locals import *
from pygame import mixer

from rich import print
from rich.traceback import install
install(show_locals=False)

# Colours
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
BLACK  = (0, 0, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Window
WIN_WIDTH = 1500
WIN_HIGHT = 1000

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HIGHT))
pygame.display.set_caption(f'PySpace Invaders 2D')

BACKGROUND = pygame.image.load(os.path.join('images', 'background.jpg'))

pygame.mouse.set_visible(False)

# Main character
SPACESHIP_WIDTH = 1982
SPACESHIP_HIGHT = 1857
SPACESHIP_SCALE = 15
SPACESHIP_SCALED_WIDTH = SPACESHIP_WIDTH/SPACESHIP_SCALE
SPACESHIP_SCALED_HIGHT = SPACESHIP_HIGHT/SPACESHIP_SCALE
SPACESHIP_START_POSITION = (WIN_WIDTH/2-(SPACESHIP_SCALED_WIDTH)/2, WIN_HIGHT-SPACESHIP_SCALED_HIGHT-50)
SPACESHIP_CENTER_OFFSET_X = SPACESHIP_SCALED_WIDTH/2
SPACESHIP_CENTER_OFFSET_Y = SPACESHIP_SCALED_HIGHT/2

SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join('images', 'spaceship.png')), (SPACESHIP_WIDTH/SPACESHIP_SCALE, SPACESHIP_HIGHT/SPACESHIP_SCALE))

#shot
PLAZMA_SHOT_WIDTH = 16
PLAZMA_SHOT_HIGHT = 29
PLAZMA_SHOT = pygame.image.load(os.path.join('images', 'shot.png'))
SHOT_SPEED = 10

#asteroid
ASTEROID_WIDTH = 1848
ASTEROID_HIGHT = 1792
ASTEROID_MIN_SCALE = 15
ASTEROID_MAX_SCALE = 100
ASTEROID = pygame.image.load(os.path.join('images', 'asteroid.png'))
ASTEROID_MAX_SPEED = 10
ASTEROID_MAX_GEN_AMOUNT = 5
ASTEROID_INIT_DELAY = 5 #s
ASTEROID_MIN_DELAY = 0.5 #s
ASTEROID_AMOUNT_PER_TIER = 10