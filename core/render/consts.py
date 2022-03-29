import os


class WindowConsts:
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720


class RenderConsts:
    FRAGMENT_SHADER_DATA_PATH = os.path.join("core", "render", "shaders", "fragment.glsl")
    VERTEX_SHADER_DATA_PATH = os.path.join("core", "render", "shaders", "vertex.glsl")
