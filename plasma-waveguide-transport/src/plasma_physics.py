import numpy as np
from scipy.constants import c, e, m_e, epsilon_0, k

def plasma_frequencies(n_e, B):
    omega_p = np.sqrt(n_e * e**2 / (epsilon_0 * m_e))
    omega_c = e * B / m_e
    return omega_p, omega_c

def whistler_group_velocity(omega, n_e, B):
    omega_p, omega_c = plasma_frequencies(n_e, B)

    # Full whistler dispersion relation for accuracy
    # n^2 = 1 + X where X = omega_p^2 / (omega * (omega_c - omega))
    # This ensures v_g < c even when approximations break down

    # Cyclotron resonance factor
    denom = omega * (omega_c - omega)
    # Avoid division by zero or negative if omega >= omega_c (though physics implies evanescent)
    # For this simulation we assume omega < omega_c

    X = omega_p**2 / denom

    # Group velocity derivation from dispersion relation
    # v_g = c / (n + omega * dn/domega)
    # Leads to:
    numerator = c * np.sqrt(1 + X)
    denominator = 1 + X * omega_c / (2 * (omega_c - omega))

    return numerator / denominator

def ponderomotive_pressure(E0):
    return epsilon_0 * E0**2 / 4

def thermal_pressure(n_e, T_e):
    return n_e * k * T_e

def wakefield_gradient(n_e):
    omega_p = np.sqrt(n_e * e**2 / (epsilon_0 * m_e))
    return m_e * c * omega_p / e
