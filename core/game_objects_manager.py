from game_modules.objects.cube import Cube
from game_modules.objects.grid_line import GridLine


class GameObjectsManager:
    def __init__(self, game):
        self.game = game

        self.world_objects = []

    def spawn_cube(self):
        self.world_objects.append(Cube(position=[1, 1, 0], eulers=[0, 0, 0]))

    def spawn_grid_lines(self):
        self.world_objects.append(
            GridLine(position=[0, 0, 0], eulers=[0, 0, 0], x_pos=0, y_pos=0, z_pos=1, color=[0, 0, 1]))
        self.world_objects.append(
            GridLine(position=[0, 0, 0], eulers=[0, 0, 0], x_pos=0, y_pos=1, z_pos=0, color=[0, 1, 0]))
        self.world_objects.append(
            GridLine(position=[0, 0, 0], eulers=[0, 0, 0], x_pos=1, y_pos=0, z_pos=0, color=[1, 0, 0]))

    def update_world_objects(self):
        for obj in self.world_objects:
            obj.update(self.game.delta_time)

            if isinstance(obj, Cube):
                obj.rotate(self.game.delta_time, [10, 0, 10])
