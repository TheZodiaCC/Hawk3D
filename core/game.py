import pygame as pg
import time
from core.render.consts import WindowConsts
from core.consts import GameConsts
from core.render.display import Display

from core.game_modules.objects.cube import Cube


class Game:
    def __init__(self):
        self.display = Display(WindowConsts.WINDOW_WIDTH, WindowConsts.WINDOW_HEIGHT, "")
        self.is_running = False

        self.clock = pg.time.Clock()
        self.delta_time = 0

        self.world_objects = []

    def init(self):
        pg.init()

        self.display.init()

        self.is_running = True

    def mainloop(self):
        prev_time = time.time()

        # Tests
        self.world_objects.append(Cube(position=[0, 0, -3], eulers=[0, 0, 0]))
        #

        while self.is_running:
            self.clock.tick(GameConsts.FPS_CAP)

            prev_time = self.calculate_delta_time(prev_time)
            self.handle_events(pg.event.get())

            self.world_objects[0].eulers[2] += 10 * self.delta_time
            self.world_objects[0].eulers[0] += 10 * self.delta_time

            if self.world_objects[0].eulers[2] > 360:
                self.world_objects[0].eulers[2] -= 360

            if self.world_objects[0].eulers[0] > 360:
                self.world_objects[0].eulers[0] -= 360

            self.display.update_display_caption(str(int(self.clock.get_fps())))

            self.display.update(self.world_objects)

        self.quit()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.is_running = False

    def calculate_delta_time(self, prev_time):
        now = time.time()

        self.delta_time = now - prev_time

        return now

    def run(self):
        self.init()
        self.mainloop()

    def quit(self):
        if self.display is not None:
            self.display.close()

        pg.quit()
