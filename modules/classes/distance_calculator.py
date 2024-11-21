# modules/classes/distance_calculator.py
from math import sqrt
from modules.classes.particle import Particle


class DistanceCalculator:
    def __init__(self, particles):
        self.particles = particles

    def calculate_distance(self, particle1, particle2):
        """Calculate the distance between two particles"""
        return sqrt((particle1.x - particle2.x) ** 2 + (particle1.y - particle2.y) ** 2)

    def find_closest_pair(self):
        """Find the closest pair of particles"""
        min_distance = float("inf")
        closest_pair = (None, None)

        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                distance = self.calculate_distance(self.particles[i], self.particles[j])
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (self.particles[i], self.particles[j])

        return closest_pair, min_distance
