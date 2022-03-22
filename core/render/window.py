import pygame as pg


class Window:
    def __init__(self, screen_width, screen_height, screen_caption_text):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen_caption_text = screen_caption_text

        self.display = None
        self.window = None

        self.frame = None

    def init(self):
        self.display = pg.display

        self.window = self.display.set_mode((self.screen_width, self.screen_height))
        self.display.set_caption(self.screen_caption_text)

        self.frame = pg.Surface((self.screen_width, self.screen_height))

    def update_window_caption(self, caption_text):
        self.display.set_caption(caption_text)

    def update_frame(self):
        self.window.blit(self.frame, self.frame.get_rect())

    def update(self):
        self.update_frame()

        self.display.update()
