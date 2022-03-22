import pygame as pg
import OpenGL.GL as GL


class Display:
    def __init__(self, screen_width, screen_height, display_caption_text):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.display_caption_text = display_caption_text

        self.display = None
        self.window = None

    def init(self):
        self.display = pg.display

        self.window = self.display.set_mode((self.screen_width, self.screen_height), pg.OPENGL|pg.DOUBLEBUF)
        self.display.set_caption(self.display_caption_text)

        GL.glClearColor(0, 0, 0, 1)

    def update_display_caption(self, caption_text):
        self.display.set_caption(caption_text)

    def update(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        self.display.flip()
