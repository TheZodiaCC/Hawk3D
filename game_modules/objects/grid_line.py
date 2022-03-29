from game_modules.objects.object_base import ObjectBase
from core.render.objects.grid_line_mesh import GridLineMesh


class GridLine(ObjectBase):
    def __init__(self, position, eulers, x_pos, y_pos, z_pos, color):
        super().__init__(position, eulers)

        self.mesh = GridLineMesh(self.position, self.eulers, x_pos, y_pos, z_pos, color)
