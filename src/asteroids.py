from config import *
from general_cls import *


class Asteroid():
    '''Class of the asteroids'''

    def __init__(self, pos_x: int, pos_y: int, speed: Position):
        scale = random.randint(ASTEROID_MIN_SCALE, ASTEROID_MAX_SCALE)
        width = ASTEROID_WIDTH/scale
        hight = ASTEROID_HIGHT/scale

        self.skin = pygame.transform.scale(ASTEROID_IMG, (width, hight))
        self.position = Position(pos_x, pos_y)
        self.speed = speed
        self.width = width
        self.hight = hight
        self.exist = True
