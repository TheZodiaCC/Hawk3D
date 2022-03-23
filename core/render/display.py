import pygame as pg
import OpenGL.GL as GL
from core.render import utils
import pyrr
import numpy as np


class Display:
    def __init__(self, screen_width, screen_height, display_caption_text):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.display_caption_text = display_caption_text

        self.display = None
        self.window = None

        self.shader = None
        self.model_matrix_location = None

    def init(self):
        self.display = pg.display

        self.window = self.display.set_mode((self.screen_width, self.screen_height), pg.OPENGL|pg.DOUBLEBUF)
        self.display.set_caption(self.display_caption_text)

        self.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        self.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        self.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        GL.glClearColor(0, 0, 0, 1)
        GL.glEnable(GL.GL_DEPTH_TEST)

        self.init_shader()
        self.init_projections()

    def init_projections(self):
        projection_transform = pyrr.matrix44.create_perspective_projection(
            fovy=45, aspect=640 / 480,
            near=0.1, far=10, dtype=np.float32
        )

        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.shader, "projection"), 1, GL.GL_FALSE, projection_transform)
        self.model_matrix_location = GL.glGetUniformLocation(self.shader, "model")

    def update_display_caption(self, caption_text):
        self.display.set_caption(caption_text)

    def update(self, objects):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        self.render_objects(objects)

        self.display.flip()

    def close(self):
        if self.shader is not None:
            GL.glDeleteProgram(self.shader)

    def render_objects(self, objects):
        for object in objects:
            mesh = object.mesh

            GL.glUseProgram(self.shader)

            model_transform = pyrr.matrix44.create_identity(dtype=np.float32)
            """
                pitch: rotation around x axis
                roll:rotation around z axis
                yaw: rotation around y axis
            """
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform,
                m2=pyrr.matrix44.create_from_eulers(
                    eulers=np.radians(object.eulers), dtype=np.float32
                )
            )
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform,
                m2=pyrr.matrix44.create_from_translation(
                    vec=np.array(object.position), dtype=np.float32
                )
            )

            GL.glUniformMatrix4fv(self.model_matrix_location, 1, GL.GL_FALSE, model_transform)

            GL.glBindVertexArray(mesh.vao)
            GL.glDrawArrays(GL.GL_TRIANGLES, 0, mesh.vertices_count)

    def init_shader(self):
        fragment_data = utils.load_shader("core/render/shaders/fragment.frag")
        vertex_data = utils.load_shader("core/render/shaders/vertex.vert")

        self.shader = utils.compile_shader(vertex_data, fragment_data)

        GL.glUseProgram(self.shader)
