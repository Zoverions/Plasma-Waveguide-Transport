import matplotlib.pyplot as plt
import numpy as np

def plot_group_velocity(frequencies, group_velocities, ax=None):
    """
    Plot group velocity versus frequency.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))

    # Convert to GHz and c
    freq_ghz = frequencies / 1e9
    vg_c = group_velocities / 299792458.0 # c

    ax.plot(freq_ghz, vg_c, linewidth=2, label='Whistler Mode Group Velocity')
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('Group Velocity (v_g / c)')
    ax.set_title('Group Velocity vs Frequency')
    ax.grid(True, which='both', linestyle='--', alpha=0.7)
    ax.legend()
    return ax

def plot_channel_condition(ponderomotive_pressure, thermal_pressure, ax=None):
    """
    Bar chart comparing ponderomotive and thermal pressures.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))

    pressures = [ponderomotive_pressure, thermal_pressure]
    labels = ['Ponderomotive\nPressure', 'Thermal\nPressure']
    colors = ['#1f77b4', '#d62728']

    bars = ax.bar(labels, pressures, color=colors)
    ax.set_ylabel('Pressure (Pa)')
    ax.set_title('Channel Formation Condition')

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2e} Pa',
                ha='center', va='bottom')

    return ax

def visualize_simulation(results, output_path=None):
    """
    Visualize the results of a single simulation run.

    Args:
        results (dict): Output from PlasmaChannel.run_simulation
        output_path (str, optional): Path to save the figure.
    """
    frequencies = results['transport']['frequencies']
    group_velocities = results['transport']['group_velocities']
    ponderomotive = results['channel_formation']['ponderomotive_pressure']
    thermal = results['channel_formation']['thermal_pressure']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    plot_group_velocity(frequencies, group_velocities, ax=ax1)
    plot_channel_condition(ponderomotive, thermal, ax=ax2)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)

    return fig
