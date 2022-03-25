import pygame as pg


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

                self.game.camera.update_direction(2 * (self.game.display.screen_width / 2 - x) * self.game.delta_time)

                pg.mouse.set_pos(self.game.display.screen_width / 2, self.game.display.screen_height / 2)

    def handle_keys(self):
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            self.game.camera.move(0, self.game.delta_time)

        if key[pg.K_s]:
            self.game.camera.move(180, self.game.delta_time)

        if key[pg.K_a]:
            self.game.camera.move(90, self.game.delta_time)

        if key[pg.K_d]:
            self.game.camera.move(-90, self.game.delta_time)

    def handle_buttons(self, key):
        if key == pg.K_ESCAPE:
            self.switch_mouse_lock()

            pg.mouse.set_visible(not self.is_mouse_locked)
