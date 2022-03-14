from config import *
from dataclasses import dataclass


@dataclass
class Position:
    '''Dataclass used to store position of objects'''

    x: int
    y: int

    def get(self) -> (int, int):
        return (self.x, self.y)


class PlazmaShot():
    '''Class of the "plazma shot" objects created when spaceship shots'''

    def __init__(self, pos_x, pos_y):

        self.skin = PLAZMA_SHOT_IMG
        self.position = Position(pos_x, pos_y)
        self.width = PLAZMA_SHOT_WIDTH
        self.hight = PLAZMA_SHOT_HIGHT
        self.exist = True

    def check_collision(self, asteroid) -> int:

        asteroid_shot = 0

        asteorid_left_x = asteroid.position.x
        asteorid_right_x = asteroid.position.x + asteroid.width
        asteorid_y = asteroid.position.y + asteroid.hight

        shot_top_center = Position(self.position.x + self.width/2, self.position.y)

        if (asteorid_left_x < shot_top_center.x < asteorid_right_x):
            if(shot_top_center.y < asteorid_y):
                asteroid.exist = False
                self.exist = False
                asteroid_shot = 1

        return asteroid_shot


class SpaceShip():
    '''Class of the spaceship'''

    def __init__(self):
        self.skin = SPACESHIP_IMG
        self.position = Position(SPACESHIP_START_X, SPACESHIP_START_Y)
        self.width = SPACESHIP_SCALED_WIDTH
        self.hight = SPACESHIP_SCALED_HIGHT
        self.exist = True
        self.stage = 0
        self.score = 0

    def shot(self) -> PlazmaShot:
        if self.exist is True:
            mause_x, mause_y = pygame.mouse.get_pos()
            return PlazmaShot(mause_x-PLAZMA_SHOT_WIDTH/2, mause_y)

    def check_collision(self, asteroid, stage, score):

        if self.exist is True:
            ship_left_x = self.position.x
            ship_right_x = self.position.x + self.width
            ship_top_y = self.position.y
            ship_bottom_y = self.position.y + self.hight

            asteroid_left_x = asteroid.position.x
            asteroid_right_x = asteroid.position.x + asteroid.width
            asteroid_top_y = asteroid.position.y
            asteroid_bottom_y = asteroid.position.y + asteroid.hight

            if ship_left_x <= asteroid_left_x <= ship_right_x or ship_left_x <= asteroid_right_x <= ship_right_x:
                if ship_top_y <= asteroid_top_y <= ship_bottom_y or ship_top_y <= asteroid_bottom_y <= ship_bottom_y:
                    asteroid.exist = False
                    self.exist = False
                    self.stage = stage
                    self.score = score


class Asteroid():
    '''Class of the asteroids'''

    def __init__(self, pos_x, pos_y, speed):
        scale = random.randint(ASTEROID_MIN_SCALE, ASTEROID_MAX_SCALE)
        width = ASTEROID_WIDTH/scale
        hight = ASTEROID_HIGHT/scale

        self.skin = pygame.transform.scale(ASTEROID_IMG, (width, hight))
        self.position = Position(pos_x, pos_y)
        self.speed = speed
        self.width = width
        self.hight = hight
        self.exist = True
