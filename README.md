# Particle Proximity Distribution Analyzer

This project computes the distribution of distances between the two closest particles among a large number of microparticles. The application is built in Python and designed for efficiency and reproducibility, making it suitable for both academic research and industrial simulations.

## Features

- Measure distances between the two closest particles in a set of microparticles.
- Compute and analyze distributions for repeated measurements.
- Lightweight, modular, and easy to extend.
- Includes decorators for measuring function execution time.
- Configuration file (`config.json`) for centralized control of parameters.
- Simplified dependency management with updated `requirements.txt`.

## Requirements

- Python 3.8+  
- Virtual environment recommended for dependency management.  

## Installation and Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/AleCornejoR/particle-proximity-distribution.git
   cd particle-proximity-distribution
   ```

2. Activate the virtual environment (if not already active):  
   ```bash
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Generate the particle data** (if not already generated):
   ```bash
   python scripts/generate_random_particles.py
   ```

2. **Run the main script**:  
   ```bash
   python main.py
   ```

3. *Still working on the output.*

## File Structure

- `main.py`: The main entry point for the application.
- `modules/`: Contains modular Python scripts for reusable functionality.
- `modules/decorators/`: Directory for custom decorators like timing function execution.
- `data/`: Directory for input particle data.
- `output/`: Directory for generated distributions and analysis results.
- `config/`: Contains the `config.json` file for centralized configuration.

## Contributing

Contributions are welcome! Please ensure that your code follows Python's PEP 8 style guidelines. Submit pull requests with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Inspired by challenges in microparticle analysis and proximity computation techniques in scientific research.

---

*Developed by Rafael Cornejo.*
