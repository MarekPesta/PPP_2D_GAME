# Libs
import os
import random
import time
from math import acos, sqrt, pi

import pygame
from pygame.locals import *
from pygame import mixer

from rich import print
from rich.traceback import install
install(show_locals=False)


# Colors
WHITE = (255, 255, 255)

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

# Main character - stpaceship
SPACESHIP_WIDTH = 1982
SPACESHIP_HIGHT = 1857
SPACESHIP_SCALE = 15
SPACESHIP_SCALED_WIDTH = SPACESHIP_WIDTH/SPACESHIP_SCALE
SPACESHIP_SCALED_HIGHT = SPACESHIP_HIGHT/SPACESHIP_SCALE
SPACESHIP_START_X = WIN_WIDTH/2 - (SPACESHIP_SCALED_WIDTH)/2
SPACESHIP_START_Y = WIN_HIGHT - SPACESHIP_SCALED_HIGHT - 50
SPACESHIP_CENTER_OFFSET_X = SPACESHIP_SCALED_WIDTH/2
SPACESHIP_CENTER_OFFSET_Y = SPACESHIP_SCALED_HIGHT/2

SPACESHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join('images', 'spaceship.png')), (SPACESHIP_WIDTH/SPACESHIP_SCALE, SPACESHIP_HIGHT/SPACESHIP_SCALE))

# Plazma shot
RED_PLAZMA_SHOT_WIDTH = 16
RED_PLAZMA_SHOT_HIGHT = 29
RED_PLAZMA_SHOT_IMG = pygame.image.load(os.path.join('images', 'red_shot.png'))
RED_PLAZMA_SHOT_SPEED = 10

GREEN_PLAZMA_SHOT_WIDTH = 18
GREEN_PLAZMA_SHOT_HIGHT = 31
GREEN_PLAZMA_SHOT_IMG = pygame.image.load(os.path.join('images', 'green_shot.png'))
GREEN_PLAZMA_SHOT_SPEED = 10

BLUE_PLAZMA_SHOT_WIDTH = 20
BLUE_PLAZMA_SHOT_HIGHT = 19
BLUE_PLAZMA_SHOT_IMG = pygame.image.load(os.path.join('images', 'blue_shot.png'))
BLUE_PLAZMA_SHOT_SPEED = 10

BOOSTER_WIDTH = 40
BOOSTER_HIGHT = 40
RED_BOOSTER_IMG = pygame.image.load(os.path.join('images', 'red_booster.png'))
GREEN_BOOSTER_IMG = pygame.image.load(os.path.join('images', 'green_booster.png'))
BLUE_BOOSTER_IMG = pygame.image.load(os.path.join('images', 'blue_booster.png'))
GUN_BOOSTER_IMG = pygame.image.load(os.path.join('images', 'gun_booster.png'))
BOOSTER_SPEED = 1
BOOSTER_LEFT_BORDER = 10
BOOSTER_RIGHT_BORDER = WIN_WIDTH - 10
BOOSTER_MIN_DELAY = 25
BOOSTER_MAX_DELAY = 60

# Asteroid
ASTEROID_WIDTH = 1848
ASTEROID_HIGHT = 1792
ASTEROID_MIN_SCALE = 15
ASTEROID_MAX_SCALE = 100
ASTEROID_IMG = pygame.image.load(os.path.join('images', 'asteroid.png'))
ASTEROID_MAX_SPEED = 10
ASTEROID_MAX_GEN_AMOUNT_INIT = 7#5
ASTEROID_MAX_GEN_AMOUNT = ASTEROID_MAX_GEN_AMOUNT_INIT
ASTEROID_INIT_DELAY = 5  #s
ASTEROID_MIN_DELAY = 0.5  #s
ASTEROID_AMOUNT_PER_TIER = 10
