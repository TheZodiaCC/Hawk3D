from core.render.objects.mesh_base import MeshBase
import numpy as np
import OpenGL.GL as GL
import ctypes


class CubeMesh(MeshBase):
    def __init__(self, position, eulers):

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

        super().__init__(self.vertices, position, eulers)

    def init_gl(self):
        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)

        self.vbo = GL.glGenBuffers(1)

        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL.GL_STATIC_DRAW)

        GL.glEnableVertexAttribArray(0)
        # vertexPos location in vertex shader | vertices count | FLOAT | FALSE | number fo bytes (6 x 4 bytes) |
        # buffer stride in bytes
        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(0))

        # vertexColor location in vertex shader | colors count | FLOAT | FALSE | number fo bytes (6 x 4 bytes) |
        # buffer stride in bytes

        GL.glEnableVertexAttribArray(1)
        GL.glVertexAttribPointer(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(12))
