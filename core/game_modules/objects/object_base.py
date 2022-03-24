import numpy as np


class ObjectBase:
    def __init__(self, position, eulers):
        self.position = np.array(position, dtype=np.float32)
        self.eulers = np.array(eulers, dtype=np.float32)

        self.mesh = None

    def update(self, dt):
        pass

    def rotate(self, dt, rotation_data=None):
        # rotation_data
        # x y z
        # value = rotation speed

        if rotation_data is not None:
            for axis_id, rotation in enumerate(rotation_data):
                self.eulers[axis_id] += rotation * dt

            self.normalize_rotation()

            self.mesh.update()

    def normalize_rotation(self):
        for i, e in enumerate(self.eulers):
            if e > 360:
                self.eulers[i] -= 360
