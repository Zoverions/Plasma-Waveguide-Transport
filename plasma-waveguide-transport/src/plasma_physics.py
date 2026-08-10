import numpy as np
from scipy.constants import c, e, m_e, epsilon_0, k


def _validated_array(value, name, *, strictly_positive=False, nonnegative=False):
    array = np.asarray(value, dtype=float)
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    if strictly_positive and np.any(array <= 0.0):
        raise ValueError(f"{name} must be greater than zero")
    if nonnegative and np.any(array < 0.0):
        raise ValueError(f"{name} must be nonnegative")
    return array


def _scalar_or_array(value):
    return float(value) if np.ndim(value) == 0 else value


def plasma_frequencies(n_e, B):
    density = _validated_array(n_e, "n_e", strictly_positive=True)
    field = _validated_array(B, "B", strictly_positive=True)
    omega_p = np.sqrt(density * e**2 / (epsilon_0 * m_e))
    omega_c = e * field / m_e
    return _scalar_or_array(omega_p), _scalar_or_array(omega_c)


def whistler_group_velocity(omega, n_e, B):
    omega_p, omega_c = plasma_frequencies(n_e, B)
    angular_frequency = _validated_array(omega, "omega", strictly_positive=True)
    if np.any(angular_frequency >= omega_c):
        raise ValueError("omega must remain below the electron cyclotron frequency")

    # Parallel cold-plasma whistler branch with displacement current retained.
    # n^2 = 1 + X where X = omega_p^2 / (omega * (omega_c - omega))
    denom = angular_frequency * (omega_c - angular_frequency)
    X = omega_p**2 / denom

    # Group velocity derivation from dispersion relation
    # v_g = c / (n + omega * dn/domega)
    numerator = c * np.sqrt(1 + X)
    denominator = 1 + X * omega_c / (2 * (omega_c - angular_frequency))
    velocity = numerator / denominator

    if not np.all(np.isfinite(velocity)) or np.any(velocity <= 0.0) or np.any(velocity >= c):
        raise ValueError("computed group velocity fell outside the finite subluminal branch")
    return _scalar_or_array(velocity)


def ponderomotive_pressure(E0):
    field = _validated_array(E0, "E0", nonnegative=True)
    return _scalar_or_array(epsilon_0 * field**2 / 4)


def thermal_pressure(n_e, T_e):
    density = _validated_array(n_e, "n_e", strictly_positive=True)
    temperature = _validated_array(T_e, "T_e", nonnegative=True)
    return _scalar_or_array(density * k * temperature)


def wakefield_gradient(n_e):
    density = _validated_array(n_e, "n_e", strictly_positive=True)
    omega_p = np.sqrt(density * e**2 / (epsilon_0 * m_e))
    return _scalar_or_array(m_e * c * omega_p / e)
