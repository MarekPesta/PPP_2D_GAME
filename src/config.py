# Libs
import os
import random
import time
from math import acos, sqrt, pi

import pygame
from pygame.locals import *
from pygame import mixer
import pygame_gui

pygame.init()

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

# Menu
BUTTON_WDITH = 125
BUTTON_HIGHT = 50
BUTTON_OFFSET = 50

info_font = pygame.font.SysFont('didot.ttc', 30)
end_font = pygame.font.SysFont('didot.ttc', 150)

manager = pygame_gui.UIManager((WIN_WIDTH, WIN_HIGHT))

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIN_WIDTH/2-1.5*BUTTON_WDITH/2, WIN_HIGHT/2-3*BUTTON_HIGHT), (1.5*BUTTON_WDITH, 1.5*BUTTON_HIGHT)), text='START', manager=manager)

easy_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIN_WIDTH/2-BUTTON_WDITH/2, WIN_HIGHT/2-1*BUTTON_HIGHT+BUTTON_OFFSET), (BUTTON_WDITH, BUTTON_HIGHT)), text='EASY', manager=manager)
medium_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIN_WIDTH/2-BUTTON_WDITH/2, WIN_HIGHT/2-0+BUTTON_OFFSET), (BUTTON_WDITH, BUTTON_HIGHT)), text='MEDIUM', manager=manager)
hard_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIN_WIDTH/2-BUTTON_WDITH/2, WIN_HIGHT/2+1*BUTTON_HIGHT+BUTTON_OFFSET), (BUTTON_WDITH, BUTTON_HIGHT)), text='HARD', manager=manager)
impossible_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIN_WIDTH/2-BUTTON_WDITH/2, WIN_HIGHT/2+2*BUTTON_HIGHT+BUTTON_OFFSET), (BUTTON_WDITH, BUTTON_HIGHT)), text='IMPOSSIBLE', manager=manager)

# Game state
state = 'menu'

# Game level
game_lvl = 'EASY'

game_lvl_settings = {'EASY': 7,
                     'MEDIUM': 20,
                     'HARD': 50,
                     'IMPOSSIBLE': 75}

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
ASTEROID_MAX_GEN_AMOUNT = game_lvl_settings[game_lvl]
ASTEROID_INIT_DELAY = 5  #s
ASTEROID_MIN_DELAY = 0.5  #s
ASTEROID_AMOUNT_PER_TIER = 10
