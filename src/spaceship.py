from config import *
from shots import *
from boosters import *


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
        self.gun = Gun_Cfg(style='red', lvl=1)
        self.gun_f = PlazmaShotFactory()
        self.armory = {'red': 1,
                       'green': 1,
                       'blue': 1}

    def shot(self) -> PlazmaShot:
        if self.exist is True:
            shot_list = self.gun_f.create_shot(self.gun)
            return shot_list

    def check_collision(self, asteroid: Asteroid, stage: int, score: int):

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

    def check_boost(self, booster: Booster):

        if self.exist is True:
            ship_left_x = self.position.x
            ship_right_x = self.position.x + self.width
            ship_top_y = self.position.y
            ship_bottom_y = self.position.y + self.hight

            booster_left_x = booster.position.x
            booster_right_x = booster.position.x + booster.width
            booster_top_y = booster.position.y
            booster_bottom_y = booster.position.y + booster.hight

            if ship_left_x <= booster_left_x <= ship_right_x or ship_left_x <= booster_right_x <= ship_right_x:
                if ship_top_y <= booster_top_y <= ship_bottom_y or ship_top_y <= booster_bottom_y <= ship_bottom_y:
                    if booster.exist is True:
                        if (booster.boost == self.gun.style or booster.boost == 'gun') and self.gun.lvl < 6:
                            self.armory[self.gun.style] += 1
                            self.gun.lvl = self.armory[self.gun.style]
                        elif booster.boost != self.gun.style and booster.boost != 'gun':
                            self.gun.style = booster.boost
                            self.gun.lvl = self.armory[self.gun.style]

                        booster.exist = False
