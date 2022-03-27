# PySpace Invaders 2D

![gif](https://user-images.githubusercontent.com/54101971/158279131-66a7e544-40d6-42cc-8884-8cd4ecac3c97.gif)

## Introduction

This is a repository of simple 2D game written in python.
It is the first part of the PPP classes project.
The goal is to create some kind of "Space Invaders" game.

## Libraries and Tools

* Python 3.10.2
* [rich](https://github.com/Textualize/rich)
* [pygame](https://github.com/pygame/pygame)
* [pygame_gui](https://github.com/MyreMylar/pygame_gui)

## Instalation

1. Install python 3.10.2
2. Install needed modules with `pip`

```sh
python -m pip install rich
python -m pip install pygame
python -m pip install pygame_gui
```

3. Run main.py

```sh
python main.py
```

## Overview

This section describes main features of the game.

### Main Menu

Screen shot of the mian game menu is shown below.

![menu](https://user-images.githubusercontent.com/54101971/160297483-e5dc37f9-b972-4a72-8688-81b4fa7a179d.PNG)

Player is able to set one of four levels of difficulty: easy, menium, hard and impossible.

### Game Objective

The player controls a speceship and his task is to avoid collison with asteroids and to shoot as many object as he can.
There is no limit in game stages or points.

### Weapons

There are three types of guns and six gun levels.
To change type of weapon or upgrade it player have to collect "universal" gun booster or a gun booste which type is consistent with type of gun which is currently used.

#### Gun Levels

* Level 1

![gun_lvl1](https://user-images.githubusercontent.com/54101971/160297438-f62ecee8-460d-414a-966e-db8c3f058e6e.gif)

* Level 2

![gun_lvl2](https://user-images.githubusercontent.com/54101971/160297443-bf95ff57-eb8d-4687-8747-6a8144a7b22c.gif)

* Level 3

![gun_lvl3](https://user-images.githubusercontent.com/54101971/160297448-60f3cd96-5ed4-424b-a0da-02f16efafb02.gif)

* Level 4

![gun_lvl4](https://user-images.githubusercontent.com/54101971/160297449-2964dfb0-5e45-42ff-83a6-d1b6e2a50bd4.gif)

* Level 5

![gun_lvl5](https://user-images.githubusercontent.com/54101971/160297452-b8babace-b40a-4da7-b882-940e0eca8e4f.gif)

* Level 6

![gun_lvl6](https://user-images.githubusercontent.com/54101971/160297458-08d7a5f5-7fa0-440e-aaad-56194615cf45.gif)

#### Gun Types

* Red gun

Red gun is a default type of gun.
It is characterized by the fact that one shot can destory only one asteroid.

![gun_lvl6](https://user-images.githubusercontent.com/54101971/160297458-08d7a5f5-7fa0-440e-aaad-56194615cf45.gif))

* Green gun

Green gun is a piercing gun.
It is characterized by the fact that one shot can destory many asteroids which are in the line of the shot.

![gun_green](https://user-images.githubusercontent.com/54101971/160297473-5298696a-2b1c-4f5f-bc5b-91222a851373.gif)

* Blue gun

Blue gun is a "bouncing" gun.
It is characterized by the fact that one shot can bounce off the shot asteroid in three possible ways.
It can go straight or change its direction by +/-45 degrees.
It can destory (and bounce off) up to three asteroids.

![gun_blue](https://user-images.githubusercontent.com/54101971/160297464-0c689132-9554-41d8-86c0-07c93db5358f.gif)

#### Gun Boosters

* Red booster

Red booster changes spaceship weapon to red gun or if red gun is already used, it increases a level of the gun.
Red booster is shown below.

![red_booster](https://user-images.githubusercontent.com/54101971/160297765-e4690389-aa14-4b47-a03a-6d80568ba9a9.png=250x250)

* Green booster

Green booster changes spaceship weapon to green gun or if green gun is already used, it increases a level of the gun.
Green booster is shown below.

![green_booster](https://user-images.githubusercontent.com/54101971/160297771-391cfe71-3db0-4ed7-86ed-5e3df031122d.png)

* Blue booster

Blue booster changes spaceship weapon to blue gun or if blue gun is already used, it increases a level of the gun.
Blue booster is shown below.

![blue_booster](https://user-images.githubusercontent.com/54101971/160297778-8b332c31-7abd-4d20-aeec-2a4ab56d3748.png)

* Universal booster

Universal booster increases a level of the gun, regardless the gun type.
Universal booster is shown below.

<img src="https://user-images.githubusercontent.com/54101971/160297756-351d7fd9-2acb-4ae7-b7e2-ab5f4aeac08d.png" width="300" height="300">
