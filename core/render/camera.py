import numpy as np
import pyrr
from OpenGL import GL as GL


class Camera:
    def __init__(self, position, shader):
        self.shader = shader

        self.position = np.array(position, dtype=np.float32)
        self.movement_speed = 1

        self.theta = 0
        self.forward_vector = np.array([0, 0, 0], dtype=np.float32)
        self.up_vector = np.array([0, 0, 1], dtype=np.float32)

    def move(self, direction, dt):
        move_direction = (direction + self.theta) % 360

        self.position[0] += self.movement_speed * np.cos(np.radians(move_direction), dtype=np.float32) * dt
        self.position[1] += self.movement_speed * np.sin(np.radians(move_direction), dtype=np.float32) * dt

    def update_direction(self, direction):
        self.theta = (self.theta + direction) % 360

    def update_forward_vector(self):
        self.forward_vector[0] = np.cos(np.radians(self.theta), dtype=np.float32)
        self.forward_vector[1] = np.sin(np.radians(self.theta), dtype=np.float32)
        self.forward_vector[2] = 0

    def get_target_vector(self):
        return self.position + self.forward_vector

    def get_lookat_matrix(self):
        self.update_forward_vector()

        right_vector = pyrr.vector3.cross(self.up_vector, self.forward_vector)
        up_vector = pyrr.vector3.cross(self.forward_vector, right_vector)

        return pyrr.matrix44.create_look_at(self.position, self.get_target_vector(), up_vector, dtype=np.float32)

    def update_view(self):
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.shader, "view"), 1, GL.GL_FALSE, self.get_lookat_matrix())
