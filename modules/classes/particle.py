# modules/classes/particle.py


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Particle(x={self.x}, y={self.y})"
