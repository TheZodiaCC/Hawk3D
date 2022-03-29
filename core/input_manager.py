import pygame as pg
from core.consts import InputConsts


class InputManager:
    def __init__(self, game):
        self.game = game

        self.is_mouse_locked = False

    def init_mouse_for_camera(self):
        self.switch_mouse_lock()

        pg.mouse.set_visible(not self.is_mouse_locked)

        pg.mouse.set_pos(self.game.display.screen_width / 2, self.game.display.screen_height / 2)

    def switch_mouse_lock(self):
        self.is_mouse_locked = not self.is_mouse_locked

    def handle_mouse(self):
        if pg.mouse.get_focused():
            if self.is_mouse_locked:
                (x, y) = pg.mouse.get_pos()

                camera_vertical_direction = InputConsts.MOUSE_SENSITIVITY * (self.game.display.screen_height / 2 - y)
                camera_horizontal_direction = InputConsts.MOUSE_SENSITIVITY * (self.game.display.screen_width / 2 - x)

                self.game.camera.update_direction(camera_horizontal_direction * self.game.delta_time,
                                                  camera_vertical_direction * self.game.delta_time)

                pg.mouse.set_pos(self.game.display.screen_width / 2, self.game.display.screen_height / 2)

    def handle_keys(self):
        key = pg.key.get_pressed()

        if key[InputConsts.MOVE_FORWARD_KEY]:
            self.game.camera.move_horizontal(0, self.game.delta_time)

        if key[InputConsts.MOVE_BACKWARD_KEY]:
            self.game.camera.move_horizontal(180, self.game.delta_time)

        if key[InputConsts.MOVE_LEFT_KEY]:
            self.game.camera.move_horizontal(90, self.game.delta_time)

        if key[InputConsts.MOVE_RIGHT_KEY]:
            self.game.camera.move_horizontal(-90, self.game.delta_time)

        if key[InputConsts.MOVE_UP_KEY]:
            self.game.camera.move_vertical(1, self.game.delta_time)

        if key[InputConsts.MOVE_DOWN_KEY]:
            self.game.camera.move_vertical(-1, self.game.delta_time)

    def handle_buttons(self, key):
        if key == pg.K_ESCAPE:
            self.switch_mouse_lock()

            pg.mouse.set_visible(not self.is_mouse_locked)
