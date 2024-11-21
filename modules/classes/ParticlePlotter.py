# modules/classes/particle_plotter.py
import matplotlib.pyplot as plt


class ParticlePlotter:
    def __init__(self, particles, config=None):
        """
        Initialize the ParticlePlotter with a list of particles.

        :param particles: List of Particle objects with (x, y) coordinates.
        :param config: Optional dictionary with plot configuration.
        """
        self.particles = particles
        self.config = config or {}

    def plot_particles(self, closest_pair=None, save_path=None):
        """
        Plot all particles and optionally highlight the closest pair.

        :param closest_pair: Tuple of the two closest particles to highlight.
        :param save_path: Optional path to save the plot as an image file.
        """
        # Extract particle coordinates
        x_coords = [particle.x for particle in self.particles]
        y_coords = [particle.y for particle in self.particles]

        # Load configurations with defaults
        figsize = self.config.get("figsize", (8, 6))
        particle_color = self.config.get("particle_color", "blue")
        particle_size = self.config.get("particle_size", 50)
        closest_color = self.config.get("closest_color", "red")
        closest_line_style = self.config.get("closest_line_style", "--")
        closest_point_size = self.config.get("closest_point_size", 100)
        grid = self.config.get("grid", True)
        grid_style = self.config.get("grid_style", "-")
        axis_limits = self.config.get(
            "axis_limits", None
        )  # Optional (x_min, x_max, y_min, y_max)

        # Create the figure
        plt.figure(figsize=figsize)

        # Plot all particles
        plt.scatter(
            x_coords, y_coords, color=particle_color, s=particle_size, label="Particles"
        )

        # Highlight the closest pair if provided
        if closest_pair:
            p1, p2 = closest_pair
            plt.plot(
                [p1.x, p2.x],
                [p1.y, p2.y],
                color=closest_color,
                linestyle=closest_line_style,
                linewidth=2,
                label="Closest Pair",
            )
            plt.scatter(
                [p1.x, p2.x],
                [p1.y, p2.y],
                color=closest_color,
                s=closest_point_size,
                label="Closest Points",
            )

        # Configure grid and axis
        if grid:
            plt.grid(True, linestyle=grid_style)
        if axis_limits:
            plt.xlim(axis_limits[0], axis_limits[1])
            plt.ylim(axis_limits[2], axis_limits[3])

        # Configure plot appearance
        plt.title("Particle Distribution")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.legend()

        # Save or show the plot
        if save_path:
            plt.savefig(save_path, bbox_inches="tight")
            print(f"Plot saved to {save_path}")
        else:
            plt.show()
