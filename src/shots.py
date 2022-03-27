from config import *
from dataclasses import dataclass
from general_cls import *
from asteroids import *

@dataclass
class Gun_Cfg:
    '''Dataclass used to configure spaceship gun'''

    style: str
    lvl: int
    position: Position(0, 0)


class PlazmaShot():
    '''Class of the "plazma shot" objects created when spaceship shots'''

    skin = None
    position = None
    width = None
    hight = None
    exist = True
    sound = None
    speed = Position(0, 0)
    style = None
    bounce = None

    def play_sound(self):
        pygame.mixer.Sound.play(self.sound)

    def change_position(self, x: int, y: int):
        self.position.x = x
        self.position.y = y

        return self

    def check_collision(self, asteroid: Asteroid):

        asteroid_shot = 0

        if self.exist is True:

            if self.width < asteroid.width:
                smaller_obj = self
                bigger_obj = asteroid
            else:
                smaller_obj = asteroid
                bigger_obj = self

            b_left_x = bigger_obj.position.x
            b_right_x = bigger_obj.position.x + bigger_obj.width
            b_top_y = bigger_obj.position.y
            b_bottom_y = bigger_obj.position.y + bigger_obj.hight

            s_left_x = smaller_obj.position.x
            s_right_x = smaller_obj.position.x + smaller_obj.width
            s_top_y = smaller_obj.position.y
            s_bottom_y = smaller_obj.position.y + smaller_obj.hight

            if b_left_x <= s_left_x <= b_right_x or b_left_x <= s_right_x <= b_right_x:
                if b_top_y <= s_top_y <= b_bottom_y or b_top_y <= s_bottom_y <= b_bottom_y:
                    asteroid.exist = False
                    asteroid_shot = 1

                    match self.style:
                        case 'red':
                            self.exist = False
                        case 'green':
                            self.exist = True
                        case 'blue':
                            if self.bounce > 0:
                                self.speed.x = random.randint(-1, 1) * self.speed.y
                                self.bounce -= 1
                            else:
                                self.exist = False

        return asteroid_shot


class RedPlazmaShot(PlazmaShot):
    '''Class of the "red plazma shot" objects created when spaceship shots'''

    def __init__(self, pos_x: int, pos_y: int):

        self.skin = RED_PLAZMA_SHOT_IMG
        self.position = Position(pos_x, pos_y)
        self.width = RED_PLAZMA_SHOT_WIDTH
        self.hight = RED_PLAZMA_SHOT_HIGHT
        self.exist = True
        self.sound = pygame.mixer.Sound(os.path.join('music', 'red_shot.wav'))
        self.speed = Position(0, RED_PLAZMA_SHOT_SPEED)
        self.style = 'red'


class GreenPlazmaShot(PlazmaShot):
    '''Class of the "green plazma shot" objects created when spaceship shots'''

    def __init__(self, pos_x: int, pos_y: int):

        self.skin = GREEN_PLAZMA_SHOT_IMG
        self.position = Position(pos_x, pos_y)
        self.width = GREEN_PLAZMA_SHOT_WIDTH
        self.hight = GREEN_PLAZMA_SHOT_HIGHT
        self.exist = True
        self.sound = pygame.mixer.Sound(os.path.join('music', 'red_shot.wav'))
        self.speed = Position(0, GREEN_PLAZMA_SHOT_SPEED)
        self.style = 'green'


class BluePlazmaShot(PlazmaShot):
    '''Class of the "green plazma shot" objects created when spaceship shots'''

    def __init__(self, pos_x: int, pos_y: int):

        self.skin = BLUE_PLAZMA_SHOT_IMG
        self.position = Position(pos_x, pos_y)
        self.width = BLUE_PLAZMA_SHOT_WIDTH
        self.hight = BLUE_PLAZMA_SHOT_HIGHT
        self.exist = True
        self.sound = pygame.mixer.Sound(os.path.join('music', 'red_shot.wav'))
        self.speed = Position(0, BLUE_PLAZMA_SHOT_SPEED)
        self.style = 'blue'
        self.bounce = 2


class PlazmaShotFactory(PlazmaShot):

    def create_single_shot(self, gun: Gun_Cfg) -> PlazmaShot:
        pos_x, pos_y = gun.position.get()
        match gun.style:
            case 'red': shot = RedPlazmaShot(pos_x, pos_y)
            case 'green': shot = GreenPlazmaShot(pos_x, pos_y)
            case 'blue': shot = BluePlazmaShot(pos_x, pos_y)
            case _: shot = None

        shot.position.x -= shot.width/2
        return shot

    def create_shot(self, gun: Gun_Cfg):
        match gun.lvl:
            case 1:
                shot = self.create_single_shot(gun)
                shot_list = [shot.change_position(shot.position.x, shot.position.y)]
            case 2:
                shot1 = self.create_single_shot(gun)
                shot2 = self.create_single_shot(gun)
                shot1.change_position(shot1.position.x + SPACESHIP_SCALED_WIDTH/2 - 5, shot1.position.y)
                shot2.change_position(shot2.position.x - SPACESHIP_SCALED_WIDTH/2 + 5, shot2.position.y)
                shot_list = [shot1, shot2]

            case 3:
                shot1 = self.create_single_shot(gun)
                shot2 = self.create_single_shot(gun)
                shot3 = self.create_single_shot(gun)
                shot1.change_position(shot1.position.x + SPACESHIP_SCALED_WIDTH/2 - 5, shot1.position.y)
                shot2.change_position(shot2.position.x - SPACESHIP_SCALED_WIDTH/2 + 5, shot2.position.y)
                shot3.change_position(shot3.position.x, shot3.position.y - 15)
                shot_list = [shot1, shot2, shot3]

            case 4:
                shot1 = self.create_single_shot(gun)
                shot2 = self.create_single_shot(gun)
                shot3 = self.create_single_shot(gun)
                shot1.change_position(shot1.position.x + SPACESHIP_SCALED_WIDTH/2 - 15, shot1.position.y)
                shot2.change_position(shot2.position.x - SPACESHIP_SCALED_WIDTH/2 + 15, shot2.position.y)
                shot3.change_position(shot3.position.x, shot3.position.y - 15)
                shot1.speed.x = -shot1.speed.y/2
                shot2.speed.x = shot2.speed.y/2
                shot1.skin = pygame.transform.rotate(shot1.skin, -30)
                shot2.skin = pygame.transform.rotate(shot2.skin, 30)
                shot_list = [shot1, shot2, shot3]

            case 5:
                shot1 = self.create_single_shot(gun)
                shot2 = self.create_single_shot(gun)
                shot3 = self.create_single_shot(gun)
                shot4 = self.create_single_shot(gun)
                shot1.change_position(shot1.position.x + SPACESHIP_SCALED_WIDTH/2 - 5, shot1.position.y)
                shot2.change_position(shot2.position.x - SPACESHIP_SCALED_WIDTH/2 + 5, shot2.position.y)
                shot3.change_position(shot3.position.x + 15, shot3.position.y - 15)
                shot4.change_position(shot4.position.x - 15, shot4.position.y - 15)
                shot_list = [shot1, shot2, shot3, shot4]

            case 6:
                shot1 = self.create_single_shot(gun)
                shot2 = self.create_single_shot(gun)
                shot3 = self.create_single_shot(gun)
                shot4 = self.create_single_shot(gun)
                shot5 = self.create_single_shot(gun)
                shot1.change_position(shot1.position.x + SPACESHIP_SCALED_WIDTH/2 - 5, shot1.position.y)
                shot2.change_position(shot2.position.x - SPACESHIP_SCALED_WIDTH/2 + 5, shot2.position.y)
                shot3.change_position(shot3.position.x, shot3.position.y - 25)
                shot4.change_position(shot4.position.x + 20, shot4.position.y - 15)
                shot5.change_position(shot5.position.x - 20, shot5.position.y - 15)
                shot_list = [shot1, shot2, shot3, shot4, shot5]

            case _: shot_list = [None]

        shot_list[0].play_sound()
        return shot_list
