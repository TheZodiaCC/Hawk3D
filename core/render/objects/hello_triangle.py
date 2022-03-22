import OpenGL.GL as GL
import numpy as np
import ctypes


class HelloTriangle:
    def __init__(self):
        # x, y, z, r, g, b
        self.vertices = np.array((
            -1, -1, 0.0, 0.0, 1.0, 0.0,
            1, -1, 0.0, 0.0, 1.0, 0.0,
            0.0, 1, 0.0, 0.0, 0.0, 1.0
        ), dtype=np.float32)

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

    def get_vertices_count(self):
        return int(np.shape(self.vertices)[0] / 6)

    def destroy(self):
        GL.glDeleteVertexArrays(1, (self.vao,))
        GL.glDeleteBuffers(1, (self.vbo,))
