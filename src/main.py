from config import *
from vars import *

# Init baisc objest and variables
pygame.init()

sysfont = pygame.font.get_default_font()
info_font = pygame.font.SysFont('didot.ttc', 30)
end_font = pygame.font.SysFont('didot.ttc', 150)


spaceShip = SpaceShip()
run = True

start = time.time()

mixer.init()
mixer.music.load(os.path.join('music', 'main_music.mp3'))
mixer.music.play()

shot_sound = pygame.mixer.Sound(os.path.join('music', 'shot.wav'))



# Game loop
while run:
    clock.tick(FPS)

    pygame.display.update()

    # Main game logic
    for event in pygame.event.get():

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            spaceShip.position = (mouse_x - SPACESHIP_CENTER_OFFSET_X, mouse_y - SPACESHIP_CENTER_OFFSET_Y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if spaceShip.exist is True:
                shots_list.append(spaceShip.shot())
                pygame.mixer.Sound.play(shot_sound)

        if spaceShip.exist is False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    spaceShip.exist = True
                    shots_list = []
                    asteroid_list = []
                    asteroid_gen_delay = ASTEROID_INIT_DELAY
                    asteroid_gen_time = 0
                    asteroid_gen_cnt = 0
                    stage = 1
                    score = 0
                    ASTEROID_MAX_GEN_AMOUNT = 5
                    start = time.time()

        if event.type == QUIT:
            run = False

    # Asteroid objects generation
    if (asteroid_gen_cnt >= ASTEROID_AMOUNT_PER_TIER):
        asteroid_gen_cnt = 0
        if asteroid_gen_delay > 0.5:
            asteroid_gen_delay -= 0.5
        else:
            asteroid_gen_delay = ASTEROID_MIN_DELAY
            ASTEROID_MAX_GEN_AMOUNT += 1
        stage += 1

    if ((time.time() - asteroid_gen_time) > asteroid_gen_delay):
        asteroid_gen_time = time.time()
        asteroid_gen_cnt += 1
        for i in range(1, random.randint(1, ASTEROID_MAX_GEN_AMOUNT)):
            start_x = random.randint(0, WIN_WIDTH)
            start_y = -(ASTEROID_HIGHT/ASTEROID_MIN_SCALE) - random.randint(0, 200)
            speed_tmp = (time.time()-start)*0.01+1
            speed = speed_tmp if (speed_tmp < ASTEROID_MAX_SPEED) else ASTEROID_MAX_SPEED 
            #print(f'speed_tmp: {speed_tmp}; speed: {speed}')
            asteroid_list.append(Asteroid(start_x, start_y, speed))

    # Drawing objects
    WIN.blit(BACKGROUND, (0, 0))

    for asteroid in asteroid_list:
        check_ship(asteroid, spaceShip, stage, score)
        for shot in shots_list:
            score = score + check_shot(asteroid, shot)

    for asteroid in asteroid_list:
        if asteroid.exist is False:
            asteroid_list.remove(asteroid)
        elif (asteroid.position[1] > WIN_HIGHT+ASTEROID_HIGHT/ASTEROID_MIN_SCALE):
            asteroid_list.remove(asteroid)
        else:
            draw_obj(asteroid)
            asteroid.position = (asteroid.position[0], asteroid.position[1]+asteroid.speed)

    for shot in shots_list:
        if shot.exist is False:
            shots_list.remove(shot)
        elif (shot.position[1] < -PLAZMA_SHOT_HIGHT):
            shots_list.remove(shot)
        else:
            draw_obj(shot)
            shot.position = (shot.position[0], shot.position[1]-SHOT_SPEED)

    if spaceShip.exist is True:
        draw_obj(spaceShip)

    if spaceShip.exist is False:
        end_info = end_font.render(f'YOU ARE DEAD', True, WHITE)
        stage_info = info_font.render(f'You reached STAGE: {spaceShip.stage}', True, WHITE)
        score_info = info_font.render(f'Your SCORE is: {spaceShip.score}', True, WHITE)
        retry_info = info_font.render(f'Press ENTER to try again', True, WHITE)
        text_width = end_info.get_width()
        text_height = end_info.get_height()
        WIN.blit(end_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2))
        WIN.blit(stage_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2+text_height+30))
        WIN.blit(score_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2+text_height+60))
        WIN.blit(retry_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2+text_height+90))
    else:
        stage_info = info_font.render(f'STAGE: {stage}', True, WHITE)
        score_info = info_font.render(f'SCORE: {score}', True, WHITE)
        WIN.blit(stage_info, (5, WIN_HIGHT - 60))
        WIN.blit(score_info, (5, WIN_HIGHT - 30))

# End game
pygame.quit()
