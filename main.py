import json
import os
import csv
from modules.classes import (
    Particle,
    DistanceCalculatorDivideAndConquer,
    ParticlePlotter,
)


def load_config(config_path):
    """
    Load the configuration from a JSON file.

    :param config_path: Path to the config JSON file.
    :return: Parsed configuration as a dictionary.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")

    try:
        with open(config_path, mode="r") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from {config_path}: {e}")


def load_particles_from_csv(filepath):
    """
    Loads particles from a CSV file.

    :param filepath: Path to the CSV file.
    :return: List of Particle objects.
    """
    particles = []
    try:
        with open(filepath, mode="r") as file:
            reader = csv.DictReader(file)

            if "X" not in reader.fieldnames or "Y" not in reader.fieldnames:
                raise ValueError("The CSV file must contain 'X' and 'Y' columns.")

            for row in reader:
                try:
                    x = float(row["X"])
                    y = float(row["Y"])
                    particles.append(Particle(x, y))
                except (ValueError, KeyError) as e:
                    print(f"Warning: Skipped a row due to an error: {e}")
    except FileNotFoundError:
        print(f"Error: File not found at the specified path: {filepath}")
    except Exception as e:
        print(f"Unexpected error occurred while loading the CSV file: {e}")

    return particles


def format_closest_pair_result(closest_pair, min_distance):
    """
    Format the result string for the closest pair of particles.

    :param closest_pair: Tuple containing the two closest Particle objects.
    :param min_distance: The minimum distance between the closest pair.
    :return: A formatted string with the result.
    """
    p1, p2 = closest_pair
    return (
        f"\n[*] The smallest distance is {min_distance:.4f}. "
        f"\n    Particle A: ({p1.x:.4f}, {p1.y:.4f}) "
        f"\n    Particle B: ({p2.x:.4f}, {p2.y:.4f})."
        "\n"
    )


def main():
    # Load particles from the CSV file
    particles = load_particles_from_csv("data/particles_1000.csv")

    # Load configuration
    config = load_config("modules/config/config.json")
    plotter_config = config.get("particle_plotter", {})

    # Create the distance calculator
    calculator = DistanceCalculatorDivideAndConquer(particles)

    # Find the closest pair of particles
    closest_pair, min_distance = calculator.find_closest_pair()

    # Use the formatting function
    result_message = format_closest_pair_result(closest_pair, min_distance)
    print(result_message)

    # Create an instance of Plotter to display the points and closest pair
    plotter = ParticlePlotter(particles, config=plotter_config)
    plotter.plot_particles(closest_pair=closest_pair)


if __name__ == "__main__":
    main()
