import pygame as pg
import time
from core.render.consts import WindowConsts
from core.consts import GameConsts
from core.render.window import Window


class Game:
    def __init__(self):
        self.window = Window(WindowConsts.WINDOW_WIDTH, WindowConsts.WINDOW_HEIGHT, "")
        self.is_running = False

        self.clock = pg.time.Clock()
        self.delta_time = 0

    def init(self):
        pg.init()

        self.window.init()

        self.is_running = True

    def mainloop(self):
        prev_time = time.time()

        while self.is_running:
            self.clock.tick(GameConsts.FPS_CAP)

            prev_time = self.calculate_delta_time(prev_time)
            self.handle_events(pg.event.get())

            self.window.update_window_caption(str(int(self.clock.get_fps())))
            self.window.update()

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
        pg.quit()
