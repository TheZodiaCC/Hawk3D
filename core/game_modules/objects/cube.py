from core.game_modules.objects.object_base import ObjectBase
import numpy as np
from core.render.objects.cube_mesh import CubeMesh


class Cube(ObjectBase):
    def __init__(self, position, eulers):
        self.position = np.array(position, dtype=np.float32)
        self.eulers = np.array(eulers, dtype=np.float32)

        self.mesh = CubeMesh(self.position, self.eulers)
