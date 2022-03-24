from core.game_modules.objects.object_base import ObjectBase
from core.render.objects.cube_mesh import CubeMesh


class Cube(ObjectBase):
    def __init__(self, position, eulers):
        super().__init__(position, eulers)

        self.mesh = CubeMesh(self.position, self.eulers)
