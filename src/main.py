from config import *

def draw_widnow(background, spaceship, shot):

    ptin(f'??')

class SpaceShip():

    def __init__(self):
        self.skin = SPACESHIP
        self.position = SPACESHIP_START_POSITION

    def shot(self):
        mause_x, mause_y = pygame.mouse.get_pos()
        return PlazaShot(mause_x-PLAZMA_SHOT_WIDTH/2, mause_y)

class PlazaShot():

    def __init__(self, pos_x, pos_y):
        self.skin = PLAZMA_SHOT
        self.position = (pos_x, pos_y)

shots_list = []

pygame.init()

spaceShip = SpaceShip()

pygame.mouse.set_visible(False)

run = True

while run:
    clock.tick(FPS)

    pygame.display.update()

    WIN.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            spaceShip.position = (mouse_x - SPACESHIP_CENTER_OFFSET_X, mouse_y - SPACESHIP_CENTER_OFFSET_Y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            shots_list.append(spaceShip.shot())

        elif event.type == QUIT:
            run = False

    for shot in shots_list:
        WIN.blit(shot.skin, shot.position)
        shot.position = (shot.position[0], shot.position[1]-SHOT_SPEED)
    WIN.blit(spaceShip.skin, spaceShip.position)

pygame.quit()