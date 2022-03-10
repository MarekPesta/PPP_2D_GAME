from config import *

def draw_widnow():

    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(SPACESHIP, (0, 0))

pygame.init()

while True:
    clock.tick(FPS)
    draw_widnow()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


