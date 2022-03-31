import pygame as pg
import time
from core.render.consts import WindowConsts
from core.consts import GameConsts
from core.render.display import Display
from core.managers.game_objects_manager import GameObjectsManager
from core.managers.input_manager import InputManager
from core.managers.debug_manager import DebugManager
from core.render.camera import Camera


class Game:
    def __init__(self):
        self.display = Display(WindowConsts.WINDOW_WIDTH, WindowConsts.WINDOW_HEIGHT, "")
        self.is_running = False

        self.clock = pg.time.Clock()
        self.delta_time = 0

        self.camera = None

        self.input_manager = InputManager(self)
        self.objects_manager = GameObjectsManager(self)
        self.debug_manager = DebugManager(self)

    def init(self):
        pg.init()

        self.display.init()

        self.camera = Camera([0, 0, 1], self.display.shader)
        self.input_manager.init_mouse_for_camera()

        self.is_running = True

    def mainloop(self):
        prev_time = time.time()

        # Tests
        self.objects_manager.spawn_cube()
        #

        while self.is_running:
            self.clock.tick(GameConsts.FPS_CAP)
            prev_time = self.calculate_delta_time(prev_time)

            self.handle_events(pg.event.get())
            self.input_manager.handle_mouse()
            self.input_manager.handle_keys()

            self.camera.update_view()

            self.objects_manager.update_world_objects()

            self.display.update_display_caption(str(int(self.clock.get_fps())))

            self.display.update(self.objects_manager.world_objects)

        self.quit()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.is_running = False

            elif event.type == pg.KEYUP:
                self.input_manager.handle_buttons(event.key)

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
