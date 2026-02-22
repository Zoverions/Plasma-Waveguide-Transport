import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import matplotlib.pyplot as plt
from src.waveguide_simulation import PlasmaChannel
from src.visualization import visualize_simulation

def generate_example_plots():
    # Parameters from the proposal
    n_e = 1e18 # m^-3
    B = 1.0 # Tesla
    T_e = 1e5 # Kelvin (approx 10 eV)

    # Frequency range: 0.5 - 2 GHz
    frequencies = np.linspace(0.5e9, 2e9, 100)

    # Laser Intensity: 10^14 W/cm^2
    # Intensity I = 0.5 * c * epsilon_0 * E0^2
    # E0 = sqrt(2 * I / (c * epsilon_0))
    I_W_cm2 = 1e14
    I_W_m2 = I_W_cm2 * 1e4
    c_speed = 299792458.0
    epsilon_0 = 8.854187817e-12
    E0 = np.sqrt(2 * I_W_m2 / (c_speed * epsilon_0))

    # Create channel
    channel = PlasmaChannel(n_e, B, T_e)

    # Run simulation
    results = channel.run_simulation(frequencies, E0)

    # Visualize
    output_dir = os.path.join(os.path.dirname(__file__), '../figures')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, 'example_outputs.png')

    # Use a non-interactive backend
    plt.switch_backend('Agg')

    visualize_simulation(results, output_path=output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_example_plots()
