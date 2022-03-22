from config import *

from asteroids import *
from boosters import *
from general_cls import *
from shots import *
from spaceship import *

# Init baisc objest and variables
#pygame.init()

shots_list = []
asteroid_list = []
asteroid_gen_delay = ASTEROID_INIT_DELAY
asteroid_gen_time = 0
asteroid_gen_cnt = 0
booster_gen_delay = BOOSTER_MIN_DELAY
booster_gen_time = 0
stage = 1
score = 0

info_font = pygame.font.SysFont('didot.ttc', 30)
end_font = pygame.font.SysFont('didot.ttc', 150)

music = Music(vol=0.5)
music.play()

spaceShip = SpaceShip()
boosterFabric = BoosterFabric()

start_x = random.randint(BOOSTER_LEFT_BORDER, BOOSTER_RIGHT_BORDER)
start_y = -BOOSTER_HIGHT
booster = boosterFabric.generate(start_x, start_y)

start = time.time()
run = True

# Game loop
while run:
    clock.tick(FPS)

    if state == 'menu':
        time_delta = clock.tick(60)/1000.0
        pygame.mouse.set_visible(True)

    if state == 'game':
        pygame.mouse.set_visible(False)

    # Handleing user
    for event in pygame.event.get():

        if state == 'game':
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                spaceShip.position.x = mouse_x - SPACESHIP_CENTER_OFFSET_X
                spaceShip.position.y = mouse_y - SPACESHIP_CENTER_OFFSET_Y

            if event.type == pygame.MOUSEBUTTONDOWN:
                if spaceShip.exist is True:
                    for tmp_shot in spaceShip.shot():
                        shots_list.append(tmp_shot)

            if spaceShip.exist is False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        state = 'menu'
                        time_delta = clock.tick(60)/1000.0

        if event.type == QUIT:
            run = False

        if state == 'menu':
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    state = 'game'
                    spaceShip.exist = True
                    shots_list = []
                    asteroid_list = []
                    asteroid_gen_delay = ASTEROID_INIT_DELAY
                    asteroid_gen_time = 0
                    asteroid_gen_cnt = 0
                    stage = 1
                    score = 0
                    ASTEROID_MAX_GEN_AMOUNT = game_lvl_settings[game_lvl]
                    start = time.time()
                    booster_gen_time = 0
                    # spaceShip.gun = Gun_Cfg(style='red', lvl=1)
                    # spaceShip.armory = {'red': 1,
                    #                     'green': 1,
                    #                     'blue': 1}
                    spaceShip = SpaceShip()

                if event.ui_element == easy_button:
                    game_lvl = 'EASY'
                if event.ui_element == medium_button:
                    game_lvl = 'MEDIUM'
                if event.ui_element == hard_button:
                    game_lvl = 'HARD'
                if event.ui_element == impossible_button:
                    game_lvl = 'IMPOSSIBLE'

        manager.process_events(event)

    if state == 'menu':
        manager.update(time_delta)

    if state == 'game':
        # Booster objects generation
        if ((time.time() - booster_gen_time) > booster_gen_delay):
            booster_gen_time = time.time()
            booster_gen_delay = random.randint(BOOSTER_MIN_DELAY, BOOSTER_MAX_DELAY)

            start_x = random.randint(BOOSTER_LEFT_BORDER, BOOSTER_RIGHT_BORDER)
            start_y = -BOOSTER_HIGHT
            booster = boosterFabric.generate(start_x, start_y)

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
                speed_tmp = (time.time() - start) * 0.01 + 1
                speed = speed_tmp if (speed_tmp < ASTEROID_MAX_SPEED) else ASTEROID_MAX_SPEED
                asteroid_list.append(Asteroid(start_x, start_y, speed))

    # Drawing bacground
    WIN.blit(BACKGROUND, (0, 0))
    if state == 'menu':
        manager.draw_ui(WIN)
        title_info = end_font.render(f'PySpace Invaders 2D', True, WHITE)
        difficulty_info = info_font.render(f'Difficulty: {game_lvl}', True, WHITE)


        text_width = title_info.get_width()
        text_height = title_info.get_height()
        WIN.blit(title_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2-WIN_HIGHT/3))
        WIN.blit(difficulty_info, (WIN_WIDTH/2-80, WIN_HIGHT/2 + 4.5*BUTTON_HIGHT))

    if state == 'game':
        # Checking if asteroid is shot or if spaceship is destroyed
        for asteroid in asteroid_list:
            spaceShip.check_collision(asteroid, stage, score)
            for shot in shots_list:
                score += shot.check_collision(asteroid)

        # Drawing asteroids
        for asteroid in asteroid_list:
            if asteroid.exist is False:
                asteroid_list.remove(asteroid)
            elif (asteroid.position.y > WIN_HIGHT + ASTEROID_HIGHT/ASTEROID_MIN_SCALE):
                asteroid_list.remove(asteroid)
            else:
                WIN.blit(asteroid.skin, asteroid.position.get())
                asteroid.position.y = asteroid.position.y + asteroid.speed

        #Drawing shots
        for shot in shots_list:
            if shot.exist is False:
                shots_list.remove(shot)
            elif (shot.position.y < -shot.hight):
                shots_list.remove(shot)
            else:
                WIN.blit(shot.skin, shot.position.get())
                shot.position.y = shot.position.y-shot.speed.y
                shot.position.x = shot.position.x-shot.speed.x

        #Drawing booster
        spaceShip.check_boost(booster)

        if (booster.position.y > WIN_HIGHT + BOOSTER_HIGHT):
            booster.exist = False
        elif booster.exist is True:
            booster.position.y = booster.position.y + booster.speed
            WIN.blit(booster.skin, booster.position.get())

        #Drawing spaceship
        if spaceShip.exist is True:
            WIN.blit(spaceShip.skin, spaceShip.position.get())

        # End game info
        if spaceShip.exist is False:
            end_info = end_font.render(f'YOU ARE DEAD', True, WHITE)
            stage_info = info_font.render(f'You reached STAGE: {spaceShip.stage}', True, WHITE)
            score_info = info_font.render(f'Your SCORE is: {spaceShip.score}', True, WHITE)
            retry_info = info_font.render(f'Press ENTER to return to main menu', True, WHITE)
            text_width = end_info.get_width()
            text_height = end_info.get_height()
            WIN.blit(end_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2))
            WIN.blit(stage_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2+text_height+30))
            WIN.blit(score_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2+text_height+60))
            WIN.blit(retry_info, (WIN_WIDTH/2-text_width/2, WIN_HIGHT/2-text_height/2+text_height+90))

        # Stage & Socre
        else:
            stage_info = info_font.render(f'STAGE: {stage}', True, WHITE)
            score_info = info_font.render(f'SCORE: {score}', True, WHITE)
            WIN.blit(stage_info, (5, WIN_HIGHT - 60))
            WIN.blit(score_info, (5, WIN_HIGHT - 30))

    pygame.display.update()

# End game
pygame.quit()
