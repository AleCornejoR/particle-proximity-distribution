# main.py
import csv
from modules.classes.particle import Particle
from modules.classes.distance_calculator import DistanceCalculator


def load_particles_from_csv(filepath):
    particles = []
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            x = float(row["X"])
            y = float(row["Y"])
            particles.append(Particle(x, y))
    return particles


def main():
    # Load particles from the CSV file
    particles = load_particles_from_csv("data/particles.csv")

    # Create the distance calculator
    calculator = DistanceCalculator(particles)

    # Find the closest pair of particles
    closest_pair, min_distance = calculator.find_closest_pair()

    print(
        f"The smallest distance is {min_distance} between {closest_pair[0]} and {closest_pair[1]}"
    )


if __name__ == "__main__":
    main()
