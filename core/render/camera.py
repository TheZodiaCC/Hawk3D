import numpy as np
import pyrr
from OpenGL import GL as GL


class Camera:
    def __init__(self, position, shader):
        self.shader = shader

        self.position = np.array(position, dtype=np.float32)
        self.movement_speed = 1

        self.theta = 0
        self.phi = 0

        self.forward_vector = np.array([0, 0, 0], dtype=np.float32)
        self.up_vector = np.array([0, 0, 1], dtype=np.float32)

    def move_horizontal(self, direction, dt):
        move_direction = (direction + self.theta) % 360

        self.position[0] += self.movement_speed * np.cos(np.radians(move_direction), dtype=np.float32) * dt
        self.position[1] += self.movement_speed * np.sin(np.radians(move_direction), dtype=np.float32) * dt

    def move_vertical(self, step, dt):
        self.position[2] += self.movement_speed * step * dt

    def update_direction(self, horizontal_direction, vertical_direction):
        self.theta = (self.theta + horizontal_direction) % 360
        self.phi = min(max(self.phi + vertical_direction, -89), 89)

    def update_forward_vector(self):
        horizontal_cos = np.cos(np.radians(self.theta), dtype=np.float32)
        horizontal_sin = np.sin(np.radians(self.theta), dtype=np.float32)

        vertical_cos = np.cos(np.radians(self.phi), dtype=np.float32)
        vertical_sin = np.sin(np.radians(self.phi), dtype=np.float32)

        self.forward_vector[0] = horizontal_cos * vertical_cos
        self.forward_vector[1] = horizontal_sin * vertical_cos
        self.forward_vector[2] = vertical_sin

    def get_target_vector(self):
        self.update_forward_vector()

        return self.position + self.forward_vector

    def get_lookat_matrix(self):
        # right_vector = pyrr.vector3.cross(self.up_vector, self.forward_vector)
        # up_vector = pyrr.vector3.cross(self.forward_vector, right_vector)

        return pyrr.matrix44.create_look_at(self.position, self.get_target_vector(), self.up_vector, dtype=np.float32)

    def update_view(self):
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.shader, "view"), 1, GL.GL_FALSE, self.get_lookat_matrix())
