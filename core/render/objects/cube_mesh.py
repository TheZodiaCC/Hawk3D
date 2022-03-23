from core.render.objects.mesh_base import MeshBase
import OpenGL.GL as GL
import numpy as np
import ctypes
import pyrr


class CubeMesh(MeshBase):
    def __init__(self, position, eulers):
        self.position = position
        self.eulers = eulers

        self.model_transform = pyrr.matrix44.create_identity(dtype=np.float32)

        # x, y, z, r, g, b
        self.vertices = np.array((
            -0.5, -0.5, -0.5, 1, 1, 1,
            0.5, -0.5, -0.5, 1, 1, 1,
            0.5, 0.5, -0.5, 1, 1, 1,

            0.5, 0.5, -0.5, 1, 1, 1,
            -0.5, 0.5, -0.5, 1, 1, 1,
            -0.5, -0.5, -0.5, 1, 1, 1,

            -0.5, -0.5, 0.5, 1, 1, 1,
            0.5, -0.5, 0.5, 1, 1, 1,
            0.5, 0.5, 0.5, 1, 1, 1,

            0.5, 0.5, 0.5, 1, 1, 1,
            -0.5, 0.5, 0.5, 1, 1, 1,
            -0.5, -0.5, 0.5, 1, 1, 1,

            -0.5, 0.5, 0.5, 1, 1, 1,
            -0.5, 0.5, -0.5, 1, 1, 1,
            -0.5, -0.5, -0.5, 1, 1, 1,

            -0.5, -0.5, -0.5, 1, 1, 1,
            -0.5, -0.5, 0.5, 1, 1, 1,
            -0.5, 0.5, 0.5, 1, 1, 1,

            0.5, 0.5, 0.5, 1, 1, 1,
            0.5, 0.5, -0.5, 1, 1, 1,
            0.5, -0.5, -0.5, 1, 1, 1,

            0.5, -0.5, -0.5, 1, 1, 1,
            0.5, -0.5, 0.5, 1, 1, 1,
            0.5, 0.5, 0.5, 1, 1, 1,

            -0.5, -0.5, -0.5, 1, 1, 1,
            0.5, -0.5, -0.5, 1, 1, 1,
            0.5, -0.5, 0.5, 1, 1, 1,

            0.5, -0.5, 0.5, 1, 1, 1,
            -0.5, -0.5, 0.5, 1, 1, 1,
            -0.5, -0.5, -0.5, 1, 1, 1,

            -0.5, 0.5, -0.5, 1, 1, 1,
            0.5, 0.5, -0.5, 1, 1, 1,
            0.5, 0.5, 0.5, 1, 1, 1,

            0.5, 0.5, 0.5, 1, 1, 1,
            -0.5, 0.5, 0.5, 1, 1, 1,
            -0.5, 0.5, -0.5, 1, 1, 1,
        ), dtype=np.float32)

        self.vertices_count = int(len(self.vertices) / 6)

        self.vao = None
        self.vbo = None

        self.init_gl()

    def init_gl(self):
        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)

        self.vbo = GL.glGenBuffers(1)

        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL.GL_STATIC_DRAW)

        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(0))

        GL.glEnableVertexAttribArray(1)
        GL.glVertexAttribPointer(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(12))

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
