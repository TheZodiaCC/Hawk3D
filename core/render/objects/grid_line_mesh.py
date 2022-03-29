from core.render.objects.mesh_base import MeshBase
import numpy as np
import OpenGL.GL as GL


class GridLineMesh(MeshBase):
    def __init__(self, position, eulers, x_pos, y_pos, z_pos, color):

        first_vertex_pos, second_vertex_pos = self.create_vertices(x_pos, y_pos, z_pos)

        # x, y, z, r, g, b
        self.vertices = np.array((
            *first_vertex_pos, *color,
            *second_vertex_pos, *color
        ), dtype=np.float32)

        super().__init__(self.vertices, position, eulers)

        self.draw_method = GL.GL_LINES

    def create_vertices(self, x_pos, y_pos, z_pos):
        first_vertex = [x_pos, y_pos, z_pos]
        second_vertex = [c - 1 if c > 0 else c for c in first_vertex]

        return first_vertex, second_vertex
