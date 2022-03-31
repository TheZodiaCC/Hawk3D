import pygame as pg


class GameConsts:
    FPS_CAP = 120


class InputConsts:
    MOUSE_SENSITIVITY = 3

    MOVE_FORWARD_KEY = pg.K_w
    MOVE_LEFT_KEY = pg.K_a
    MOVE_RIGHT_KEY = pg.K_d
    MOVE_BACKWARD_KEY = pg.K_s
    MOVE_UP_KEY = pg.K_LSHIFT
    MOVE_DOWN_KEY = pg.K_LCTRL

    DEBUG_MODE_KEY = pg.K_DELETE
