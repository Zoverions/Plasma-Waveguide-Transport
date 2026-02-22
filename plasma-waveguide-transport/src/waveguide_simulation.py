import numpy as np
from . import plasma_physics

class PlasmaChannel:
    """
    Simulates a plasma channel for waveguide transport.
    """
    def __init__(self, n_e, B, T_e):
        """
        Initialize the plasma channel.

        Args:
            n_e (float): Electron density in m^-3
            B (float): Magnetic field in Tesla
            T_e (float): Electron temperature in Kelvin
        """
        self.n_e = n_e
        self.B = B
        self.T_e = T_e

    def check_channel_formation(self, E0):
        """
        Check if the ponderomotive pressure exceeds the thermal pressure,
        which is the condition for channel formation.

        Args:
            E0 (float): Electric field amplitude in V/m

        Returns:
            dict: {
                'formed': bool,
                'ponderomotive_pressure': float,
                'thermal_pressure': float
            }
        """
        p_pond = plasma_physics.ponderomotive_pressure(E0)
        p_therm = plasma_physics.thermal_pressure(self.n_e, self.T_e)

        return {
            'formed': p_pond > p_therm,
            'ponderomotive_pressure': p_pond,
            'thermal_pressure': p_therm
        }

    def calculate_group_velocity(self, frequencies):
        """
        Calculate group velocity for a given array of frequencies.

        Args:
            frequencies (np.array): Frequencies in Hz

        Returns:
            np.array: Group velocity in m/s
        """
        omegas = 2 * np.pi * frequencies
        return plasma_physics.whistler_group_velocity(omegas, self.n_e, self.B)

    def calculate_wakefield_gradient(self):
        """
        Calculate the wakefield acceleration gradient.

        Returns:
            float: Gradient in V/m
        """
        return plasma_physics.wakefield_gradient(self.n_e)

    def run_simulation(self, frequencies, E0):
        """
        Run a full simulation for a set of frequencies and a given field amplitude.

        Args:
            frequencies (np.array): Frequencies in Hz
            E0 (float): Electric field amplitude in V/m

        Returns:
            dict: Simulation results
        """
        channel_status = self.check_channel_formation(E0)
        group_velocities = self.calculate_group_velocity(frequencies)
        wakefield = self.calculate_wakefield_gradient()

        return {
            'parameters': {
                'n_e': self.n_e,
                'B': self.B,
                'T_e': self.T_e,
                'E0': E0
            },
            'channel_formation': channel_status,
            'transport': {
                'frequencies': frequencies,
                'group_velocities': group_velocities
            },
            'acceleration': {
                'wakefield_gradient': wakefield
            }
        }
