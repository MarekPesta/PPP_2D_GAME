from config import *

# classes
class SpaceShip():

    def __init__(self):
        self.skin = SPACESHIP
        self.position = SPACESHIP_START_POSITION
        self.width = SPACESHIP_SCALED_WIDTH
        self.hight = SPACESHIP_SCALED_HIGHT
        self.exist = True
        self.stage = 0
        self.score = 0

    def shot(self):
        if self.exist is True:
            mause_x, mause_y = pygame.mouse.get_pos()
            return PlazmaShot(mause_x-PLAZMA_SHOT_WIDTH/2, mause_y)

class PlazmaShot():

    def __init__(self, pos_x, pos_y):
        self.skin = PLAZMA_SHOT
        self.position = (pos_x, pos_y)
        self.width = PLAZMA_SHOT_WIDTH
        self.hight = PLAZMA_SHOT_HIGHT
        self.exist = True

class Asteroid():

    def __init__(self, pos_x, pos_y, speed):
        scale = random.randint(ASTEROID_MIN_SCALE, ASTEROID_MAX_SCALE)
        # print(scale)
        width = ASTEROID_WIDTH/scale
        hight = ASTEROID_HIGHT/scale

        self.skin = pygame.transform.scale(ASTEROID, (width, hight))
        self.position = (pos_x, pos_y)
        self.speed = speed
        self.width = width
        self.hight = hight
        self.exist = True


# funcrions
def draw_obj(obj):

    WIN.blit(obj.skin, obj.position)


def check_shot(asteroid, shot):

    asteorid_border_left_x = asteroid.position[0]
    asteorid_border_right_x = asteroid.position[0]+asteroid.width
    asteorid_border_y = asteroid.position[1]+asteroid.hight

    shot_center = (shot.position[0]+shot.width/2, shot.position[1])

    if (asteorid_border_left_x < shot_center[0] and asteorid_border_right_x > shot_center[0]):
        if(asteorid_border_y > shot_center[1]):
            asteroid.exist = False
            shot.exist = False

            return 1
        else:
            return 0
    else:
        return 0


def check_ship(asteroid, ship, stage, score):

    if ship.exist is True:
        ship_left_x = ship.position[0]
        ship_right_x = ship.position[0]+ship.width
        ship_top_y = ship.position[1]
        ship_bottom_y = ship.position[1]+ship.hight

        asteroid_left_x = asteroid.position[0]
        asteroid_right_x = asteroid.position[0]+asteroid.width
        asteroid_top_y = asteroid.position[1]
        asteroid_bottom_y = asteroid.position[1]+asteroid.hight

        if ship_left_x <= asteroid_left_x <= ship_right_x or ship_left_x <= asteroid_right_x <= ship_right_x:
            if ship_top_y <= asteroid_top_y <= ship_bottom_y or ship_top_y <= asteroid_bottom_y <= ship_bottom_y:
                asteroid.exist = False
                ship.exist = False
                ship.stage = stage
                ship.score = score

# variables
shots_list = []
asteroid_list = []
asteroid_gen_delay = ASTEROID_INIT_DELAY
asteroid_gen_time = 0
asteroid_gen_cnt = 0
stage = 1
score = 0
