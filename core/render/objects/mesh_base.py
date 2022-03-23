import pyrr
import OpenGL.GL as GL
import numpy as np


class MeshBase:
    def __init__(self, vertices, position, eulers):
        self.vertices = vertices

        self.position = position
        self.eulers = eulers

        self.model_transform = pyrr.matrix44.create_identity(dtype=np.float32)

        self.vertices_count = int(len(self.vertices) / 6)

        self.vao = None
        self.vbo = None

        self.init_gl()

    def init_gl(self):
        # Implemented by every mesh class
        pass

    def update(self):
        self.update_model_transformation()

    def update_model_transformation(self):
        self.model_transform = pyrr.matrix44.create_identity(dtype=np.float32)

        self.model_transform = pyrr.matrix44.multiply(
            m1=self.model_transform,
            m2=pyrr.matrix44.create_from_eulers(
                eulers=np.radians(self.eulers), dtype=np.float32
            )
        )

        self.model_transform = pyrr.matrix44.multiply(
            m1=self.model_transform,
            m2=pyrr.matrix44.create_from_translation(
                vec=np.array(self.position), dtype=np.float32
            )
        )

    def destroy(self):
        GL.glDeleteVertexArrays(1, (self.vao,))
        GL.glDeleteBuffers(1, (self.vbo,))
