# Particle Proximity Distribution Analyzer

This project computes the distribution of distances between the two closest particles among a large number of microparticles. The application is built in Python and designed for efficiency and reproducibility, making it suitable for use in both academic research and industrial simulations.

## Features

- Measure distances between the two closest particles in a set of microparticles.
- Compute and analyze distributions for repeated measurements.
- Lightweight, modular, and easy to extend.

## Requirements

- Python 3.8+  
- Virtual environment recommended for dependency management.  

## Installation and Setup

1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd particle-proximity-distribution-analyzer
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

1. Run the main script:  
   ```bash
   python main.py
   ```
   *(Implementation to be added later.)*

2. Output files containing the computed distributions will be saved to the `output/` directory.

## File Structure

- `main.py`: The main entry point for the application.
- `modules/`: Contains modular Python scripts for reusable functionality.
- `data/`: Directory for input particle data.
- `output/`: Directory for generated distributions and analysis results.

## Contributing

Contributions are welcome! Please ensure that your code follows Python's PEP 8 style guidelines. Submit pull requests with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


## Acknowledgments

Inspired by challenges in microparticle analysis and proximity computation techniques in scientific research.

---

*Developed by Rafael Cornejo.*

