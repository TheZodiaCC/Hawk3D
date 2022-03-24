from core.render.objects.mesh_base import MeshBase
import numpy as np


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
