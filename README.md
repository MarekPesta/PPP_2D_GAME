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

![alt text](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003556)

Player is able to set one of four levels of difficulty: easy, menium, hard and impossible.

### Game Objective

The player controls a speceship and his task is to avoid collison with asteroids and to shoot as many object as he can.
There is no limit in game stages or points.

### Weapons

There are three types of guns and six gun levels.
To change type of weapon or upgrade it player have to collect "universal" gun booster or a gun booste which type is consistent with type of gun which is currently used.

#### Gun Levels

* Level 1
![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003368)

* Level 2
![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003389)

* Level 3
![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003408)

* Level 4
![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003432)

* Level 5
![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003471)

* Level 6
![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003495)

#### Gun Types

* Red gun

Red gun is a default type of gun.
It is characterized by the fact that one shot can destory only one asteroid.

![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003495)

* Green gun

Green gun is a piercing gun.
It is characterized by the fact that one shot can destory many asteroids which are in the line of the shot.

![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003536)

* Blue gun

Blue gun is a "bouncing" gun.
It is characterized by the fact that one shot can bounce off the shot asteroid in three possible ways.
It can go straight or change its direction by +/-45 degrees.
It can destory (and bounce off) up to three asteroids.

![gif](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080003516)

#### Gun Boosters

* Red booster

Red booster changes spaceship weapon to red gun or if red gun is already used, it increases a level of the gun.
Red booster is shown below.

![alt text](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080004871)

* Green booster

Green booster changes spaceship weapon to green gun or if green gun is already used, it increases a level of the gun.
Green booster is shown below.

![alt text](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080004897)

* Blue booster

Blue booster changes spaceship weapon to blue gun or if blue gun is already used, it increases a level of the gun.
Blue booster is shown below.

![alt text](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080004919)

* Universal booster

Universal booster increases a level of the gun, regardless the gun type.
Universal booster is shown below.

![alt text](https://github.com/MarekPesta/PPP_2D_GAME/issues/1#issuecomment-1080004841)
