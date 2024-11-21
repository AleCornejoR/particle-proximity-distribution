# modules/classes/distance_calculator.py
from math import sqrt
from typing import List, Tuple, Optional
from modules.classes.Particle import Particle


class DistanceCalculatorBrute:
    def __init__(self, particles: List[Particle]):
        """
        Initialize the DistanceCalculator with a list of particles.

        :param particles: List of Particle objects.
        """
        if not particles or len(particles) < 2:
            raise ValueError(
                "At least two particles are required to calculate distances."
            )
        self.particles = particles

    def _calculate_distance(self, particle1: Particle, particle2: Particle) -> float:
        """
        Calculate the Euclidean distance between two particles.

        :param particle1: The first Particle object.
        :param particle2: The second Particle object.
        :return: The Euclidean distance as a float.
        """
        return sqrt((particle1.x - particle2.x) ** 2 + (particle1.y - particle2.y) ** 2)

    def find_closest_pair(self) -> Tuple[Tuple[Particle, Particle], float]:
        """
        Find the closest pair of particles and their distance.

        :return: A tuple containing the closest pair of particles and their distance.
        """
        min_distance = float("inf")
        closest_pair: Optional[Tuple[Particle, Particle]] = None

        # Brute force approach
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                distance = self._calculate_distance(
                    self.particles[i], self.particles[j]
                )
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (self.particles[i], self.particles[j])

        return closest_pair, min_distance


class DistanceCalculatorDivideAndConquer:
    def __init__(self, particles: List[Particle]):
        """
        Initialize the DistanceCalculator with a list of particles.

        :param particles: List of Particle objects.
        """
        if not particles or len(particles) < 2:
            raise ValueError(
                "At least two particles are required to calculate distances."
            )
        self.particles = sorted(particles, key=lambda p: p.x)

    def _calculate_distance(self, particle1: Particle, particle2: Particle) -> float:
        """Calculate the Euclidean distance between two particles."""
        return sqrt((particle1.x - particle2.x) ** 2 + (particle1.y - particle2.y) ** 2)

    def _find_closest_in_strip(
        self, strip: List[Particle], min_distance: float
    ) -> float:
        """Find the closest pair in a vertical strip."""
        strip.sort(key=lambda p: p.y)
        min_d = min_distance
        closest_pair = None

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j].y - strip[i].y >= min_d:
                    break
                distance = self._calculate_distance(strip[i], strip[j])
                if distance < min_d:
                    min_d = distance
                    closest_pair = (strip[i], strip[j])

        return closest_pair, min_d

    def _closest_recursive(
        self, particles: List[Particle]
    ) -> Tuple[Tuple[Particle, Particle], float]:
        """Recursive function for closest pair."""
        n = len(particles)
        if n <= 3:
            # Brute force for small subsets
            min_distance = float("inf")
            closest_pair = None
            for i in range(n):
                for j in range(i + 1, n):
                    distance = self._calculate_distance(particles[i], particles[j])
                    if distance < min_distance:
                        min_distance = distance
                        closest_pair = (particles[i], particles[j])
            return closest_pair, min_distance

        mid = n // 2
        left_particles = particles[:mid]
        right_particles = particles[mid:]

        closest_left, min_left = self._closest_recursive(left_particles)
        closest_right, min_right = self._closest_recursive(right_particles)

        if min_left < min_right:
            closest_pair = closest_left
            min_distance = min_left
        else:
            closest_pair = closest_right
            min_distance = min_right

        # Merge step
        mid_x = particles[mid].x
        strip = [p for p in particles if abs(p.x - mid_x) < min_distance]
        strip_closest_pair, strip_distance = self._find_closest_in_strip(
            strip, min_distance
        )

        if strip_distance < min_distance:
            return strip_closest_pair, strip_distance
        return closest_pair, min_distance

    def find_closest_pair(self) -> Tuple[Tuple[Particle, Particle], float]:
        """Find the closest pair of particles using divide-and-conquer."""
        return self._closest_recursive(self.particles)
