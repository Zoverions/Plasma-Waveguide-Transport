import matplotlib.pyplot as plt
import numpy as np

def plot_group_velocity(frequencies, vg, filename='figures/group_velocity.png'):
    """
    Plot group velocity vs frequency.

    :param frequencies: Array of frequencies (Hz)
    :param vg: Array of group velocities (m/s)
    :param filename: Output filename
    """
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies / 1e9, vg / 3e8, label='Whistler Group Velocity')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Group Velocity (c)')
    plt.title('Whistler-Mode Group Velocity')
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)
    plt.close()

def plot_channel_formation(E0_range, p_pond, p_therm, filename='figures/channel_formation.png'):
    """
    Plot channel formation condition.

    :param E0_range: Array of Electric field amplitudes (V/m)
    :param p_pond: Array of ponderomotive pressures (Pa)
    :param p_therm: Thermal pressure (Pa)
    :param filename: Output filename
    """
    plt.figure(figsize=(10, 6))
    plt.plot(E0_range / 1e6, p_pond, label='Ponderomotive Pressure')
    plt.axhline(y=p_therm, color='r', linestyle='--', label='Thermal Pressure')
    plt.xlabel('Electric Field (MV/m)')
    plt.ylabel('Pressure (Pa)')
    plt.title('Ponderomotive Channel Formation Condition')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
