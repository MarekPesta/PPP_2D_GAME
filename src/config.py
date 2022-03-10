# Libs
import os

import pygame
from pygame.locals import *

from rich import print
from rich.traceback import install
install(show_locals=False)

# Colours
BLACK  = (255, 255, 255)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Window
WIN_WIDTH  = 1500
WIN_HIGHT  = 1000

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HIGHT))
pygame.display.set_caption(f'PySpace Invaders 2D')

BACKGROUND = pygame.image.load(os.path.join('images', 'background.jpg'))

# Main character
SPACESHIP_WIDTH = 1982
SPACESHIP_HIGHT = 1857
SPACESHIP_SCALE = 15
SPACESHIP_SALED_WIDTH = SPACESHIP_WIDTH/SPACESHIP_SCALE
SPACESHIP_SCALED_HIGHT = SPACESHIP_HIGHT/SPACESHIP_SCALE
SPACESHIP_START_POSITION = (WIN_WIDTH/2-(SPACESHIP_SALED_WIDTH)/2, WIN_HIGHT-SPACESHIP_SCALED_HIGHT-50)
SPACESHIP_CENTER_OFFSET_X = SPACESHIP_SALED_WIDTH/2
SPACESHIP_CENTER_OFFSET_Y = SPACESHIP_SCALED_HIGHT/2

SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join('images', 'spaceship.png')), (SPACESHIP_WIDTH/SPACESHIP_SCALE, SPACESHIP_HIGHT/SPACESHIP_SCALE))

#shot
PLAZMA_SHOT_WIDTH = 16
PLAZMA_SHOT_HIGHT = 29
PLAZMA_SHOT = pygame.image.load(os.path.join('images', 'shot.png'))
SHOT_SPEED = 10