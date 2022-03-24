from core.game_modules.objects.cube import Cube


class GameObjectsManager:
    def __init__(self, game):
        self.game = game

        self.world_objects = []

    def spawn_cube(self):
        self.world_objects.append(Cube(position=[0, 0, -3], eulers=[0, 0, 0]))

    def update_world_objects(self):
        for obj in self.world_objects:
            obj.update(self.game.delta_time)
            obj.rotate(self.game.delta_time, [10, 0, 10])
