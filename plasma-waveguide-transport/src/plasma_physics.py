import numpy as np
from scipy.constants import c, e, m_e, epsilon_0, k

def plasma_frequencies(n_e, B):
    """
    Calculate plasma frequency and electron cyclotron frequency.

    Args:
        n_e (float): Electron density in m^-3
        B (float): Magnetic field in Tesla

    Returns:
        tuple: (omega_p, omega_c) in rad/s
    """
    omega_p = np.sqrt(n_e * e**2 / (epsilon_0 * m_e))
    omega_c = e * B / m_e
    return omega_p, omega_c

def whistler_group_velocity(omega, n_e, B):
    """
    Calculate group velocity of whistler mode.

    Uses the full R-wave dispersion relation to ensure physical correctness
    (v_g < c) even when the low-frequency approximation breaks down.

    n^2 = 1 + omega_p^2 / (omega * (omega_c - omega))
    v_g = c / (d(n*omega)/domega) = c / (n + omega * dn/domega)

    Args:
        omega (float or np.array): Angular frequency in rad/s
        n_e (float): Electron density in m^-3
        B (float): Magnetic field in Tesla

    Returns:
        float or np.array: Group velocity in m/s
    """
    omega_p, omega_c = plasma_frequencies(n_e, B)

    # R-wave dispersion relation
    # n^2 = 1 + omega_p^2 / (omega * (omega_c - omega))
    denom = omega * (omega_c - omega)

    # Handle potentially invalid inputs (though caller should ensure validity)
    # Using np.maximum to avoid division by zero or negative in sqrt if omega > omega_c
    # But for this scope, we assume omega < omega_c

    X = omega_p**2 / denom
    n = np.sqrt(1 + X)

    # Derivative dn/domega
    # d(n^2)/dw = 2n dn/dw = -omega_p^2 * (omega_c - 2omega) / (omega * (omega_c - omega))^2
    # dn/dw = (1/2n) * [ -X * (omega_c - 2omega) / denom ]

    dn_dw = -X * (omega_c - 2*omega) / (2 * n * denom)

    # Group velocity: v_g = c / (n + omega * dn/dw)
    vg = c / (n + omega * dn_dw)

    return vg

def ponderomotive_pressure(E0):
    """
    Calculate ponderomotive pressure.

    Args:
        E0 (float): Electric field amplitude in V/m

    Returns:
        float: Pressure in Pascals
    """
    return epsilon_0 * E0**2 / 4

def thermal_pressure(n_e, T_e):
    """
    Calculate thermal pressure.

    Args:
        n_e (float): Electron density in m^-3
        T_e (float): Electron temperature in Kelvin

    Returns:
        float: Pressure in Pascals
    """
    return n_e * k * T_e

def wakefield_gradient(n_e):
    """
    Calculate wakefield acceleration gradient.

    Args:
        n_e (float): Electron density in m^-3

    Returns:
        float: Electric field gradient in V/m
    """
    omega_p = np.sqrt(n_e * e**2 / (epsilon_0 * m_e))
    return m_e * c * omega_p / e
