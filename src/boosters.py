from config import *
from general_cls import *


class Booster():
    '''Class of the Booster'''

    skin = None
    position = Position(0, 0)
    speed = None
    width = None
    hight = None
    exist = None
    boost = None


class RedBooster(Booster):
    '''Class of the Red Booster'''

    def __init__(self, pos_x: int, pos_y: int):

        self.skin = pygame.transform.scale(RED_BOOSTER_IMG, (BOOSTER_WIDTH, BOOSTER_HIGHT))
        self.position = Position(pos_x, pos_y)
        self.speed = BOOSTER_SPEED
        self.width = BOOSTER_WIDTH
        self.hight = BOOSTER_HIGHT
        self.exist = True
        self.boost = 'red'


class GreenBooster(Booster):
    '''Class of the Green Booster'''

    def __init__(self, pos_x: int, pos_y: int):

        self.skin = pygame.transform.scale(GREEN_BOOSTER_IMG, (BOOSTER_WIDTH, BOOSTER_HIGHT))
        self.position = Position(pos_x, pos_y)
        self.speed = BOOSTER_SPEED
        self.width = BOOSTER_WIDTH
        self.hight = BOOSTER_HIGHT
        self.exist = True
        self.boost = 'green'


class BlueBooster(Booster):
    '''Class of the Blue Booster'''

    def __init__(self, pos_x: int, pos_y: int):

        self.skin = pygame.transform.scale(BLUE_BOOSTER_IMG, (BOOSTER_WIDTH, BOOSTER_HIGHT))
        self.position = Position(pos_x, pos_y)
        self.speed = BOOSTER_SPEED
        self.width = BOOSTER_WIDTH
        self.hight = BOOSTER_HIGHT
        self.exist = True
        self.boost = 'blue'


class GunBooster(Booster):
    '''Class of the Gun Booster'''

    def __init__(self, pos_x: int, pos_y: int):

        self.skin = pygame.transform.scale(GUN_BOOSTER_IMG, (BOOSTER_WIDTH, BOOSTER_HIGHT))
        self.position = Position(pos_x, pos_y)
        self.speed = BOOSTER_SPEED
        self.width = BOOSTER_WIDTH
        self.hight = BOOSTER_HIGHT
        self.exist = True
        self.boost = 'gun'


class BoosterFabric(Booster):
    '''Class of the Booster Fabric'''

    def generate(self, x: int, y: int):
        booster_rand = random.randint(1, 5)

        match booster_rand:
            case 1: booster = RedBooster(x, y)
            case 2: booster = GreenBooster(x, y)
            case 3: booster = BlueBooster(x, y)
            case _: booster = GunBooster(x, y)

        return booster
