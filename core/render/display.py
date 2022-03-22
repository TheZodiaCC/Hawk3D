import pygame as pg


class Display:
    def __init__(self, screen_width, screen_height, display_caption_text):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.display_caption_text = display_caption_text

        self.display = None
        self.window = None

        self.frame = None

    def init(self):
        self.display = pg.display

        self.window = self.display.set_mode((self.screen_width, self.screen_height))
        self.display.set_caption(self.display_caption_text)

        self.frame = pg.Surface((self.screen_width, self.screen_height))

    def update_display_caption(self, caption_text):
        self.display.set_caption(caption_text)

    def update_frame(self):
        self.window.blit(self.frame, self.frame.get_rect())

    def update(self):
        self.update_frame()

        self.display.update()
