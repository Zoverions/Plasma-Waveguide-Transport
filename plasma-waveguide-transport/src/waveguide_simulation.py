import numpy as np
from plasma_physics import plasma_frequencies, whistler_group_velocity, ponderomotive_pressure, thermal_pressure, wakefield_gradient

class WaveguideSimulation:
    def __init__(self, n_e, B, T_e):
        """
        Initialize the simulation with plasma parameters.

        :param n_e: Electron density (m^-3)
        :param B: Magnetic field (T)
        :param T_e: Electron temperature (K)
        """
        plasma_frequencies(n_e, B)
        thermal_pressure(n_e, T_e)
        self.n_e = n_e
        self.B = B
        self.T_e = T_e

    def simulate_group_velocity(self, frequencies):
        """
        Calculate group velocity for a range of frequencies.

        :param frequencies: Array of frequencies (Hz)
        :return: Array of group velocities (m/s)
        """
        # Convert Hz to rad/s for omega calculation
        omega = 2 * np.pi * frequencies
        return whistler_group_velocity(omega, self.n_e, self.B)

    def check_channel_formation(self, E0_range):
        """
        Check channel formation condition over a range of Electric field strengths.

        :param E0_range: Array of Electric field amplitudes (V/m)
        :return: (ponderomotive_pressures, thermal_pressure, is_formed_array)
        """
        p_pond = ponderomotive_pressure(E0_range)
        p_therm = thermal_pressure(self.n_e, self.T_e)
        return p_pond, p_therm, p_pond > p_therm

    def calculate_wakefield_gradient(self):
        """
        Calculate the wakefield acceleration gradient.

        :return: Gradient (V/m)
        """
        return wakefield_gradient(self.n_e)
