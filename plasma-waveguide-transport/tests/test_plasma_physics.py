from __future__ import annotations

import unittest

import numpy as np
from scipy.constants import c

from plasma_physics import (
    plasma_frequencies,
    ponderomotive_pressure,
    thermal_pressure,
    wakefield_gradient,
    whistler_group_velocity,
)
from waveguide_simulation import WaveguideSimulation


class PlasmaFrequencyTests(unittest.TestCase):
    def test_reference_scale_for_one_tesla_and_1e18_density(self):
        omega_p, omega_c = plasma_frequencies(1.0e18, 1.0)

        self.assertAlmostEqual(omega_p, 5.64146e10, delta=omega_p * 1.0e-5)
        self.assertAlmostEqual(omega_c, 1.75882e11, delta=omega_c * 1.0e-5)

    def test_invalid_density_or_field_is_rejected(self):
        for density, field in ((0.0, 1.0), (-1.0, 1.0), (1.0e18, 0.0), (1.0e18, -1.0)):
            with self.subTest(density=density, field=field):
                with self.assertRaises(ValueError):
                    plasma_frequencies(density, field)

    def test_nonfinite_parameters_are_rejected(self):
        for density, field in ((np.nan, 1.0), (np.inf, 1.0), (1.0e18, np.nan), (1.0e18, np.inf)):
            with self.subTest(density=density, field=field):
                with self.assertRaises(ValueError):
                    plasma_frequencies(density, field)


class WhistlerGroupVelocityTests(unittest.TestCase):
    density = 1.0e18
    field = 1.0

    def test_valid_branch_is_finite_positive_and_subluminal(self):
        _, omega_c = plasma_frequencies(self.density, self.field)
        omega = omega_c * np.geomspace(1.0e-6, 0.99, 400)

        velocity = whistler_group_velocity(omega, self.density, self.field)

        self.assertTrue(np.all(np.isfinite(velocity)))
        self.assertTrue(np.all(velocity > 0.0))
        self.assertTrue(np.all(velocity < c))

    def test_low_frequency_limit_matches_declared_approximation(self):
        omega_p, omega_c = plasma_frequencies(self.density, self.field)
        omega = omega_c * 1.0e-4
        exact = whistler_group_velocity(omega, self.density, self.field)
        approximation = 2.0 * c * np.sqrt(omega * omega_c) / omega_p

        self.assertAlmostEqual(exact / approximation, 1.0, delta=0.002)

    def test_scalar_input_returns_float(self):
        _, omega_c = plasma_frequencies(self.density, self.field)
        result = whistler_group_velocity(0.1 * omega_c, self.density, self.field)

        self.assertIsInstance(result, float)

    def test_invalid_frequency_domain_is_rejected(self):
        _, omega_c = plasma_frequencies(self.density, self.field)
        for omega in (0.0, -1.0, omega_c, 1.01 * omega_c, np.nan, np.inf):
            with self.subTest(omega=omega):
                with self.assertRaises(ValueError):
                    whistler_group_velocity(omega, self.density, self.field)

    def test_one_invalid_vector_element_rejects_the_vector(self):
        _, omega_c = plasma_frequencies(self.density, self.field)
        with self.assertRaises(ValueError):
            whistler_group_velocity(np.array([0.1 * omega_c, omega_c]), self.density, self.field)


class DerivedQuantityTests(unittest.TestCase):
    def test_pressure_and_gradient_outputs_are_positive(self):
        self.assertGreater(ponderomotive_pressure(1.0e6), 0.0)
        self.assertGreater(thermal_pressure(1.0e18, 1.0e5), 0.0)
        self.assertGreater(wakefield_gradient(1.0e18), 0.0)

    def test_invalid_derived_quantity_inputs_are_rejected(self):
        invalid_calls = (
            lambda: ponderomotive_pressure(-1.0),
            lambda: ponderomotive_pressure(np.nan),
            lambda: thermal_pressure(0.0, 1.0e5),
            lambda: thermal_pressure(1.0e18, -1.0),
            lambda: wakefield_gradient(0.0),
        )
        for call in invalid_calls:
            with self.subTest(call=call):
                with self.assertRaises(ValueError):
                    call()

    def test_simulation_reuses_validated_model_boundary(self):
        simulation = WaveguideSimulation(n_e=1.0e18, B=1.0, T_e=1.0e5)
        _, omega_c = plasma_frequencies(simulation.n_e, simulation.B)
        frequencies_hz = np.array([0.01, 0.1, 0.5]) * omega_c / (2.0 * np.pi)

        velocity = simulation.simulate_group_velocity(frequencies_hz)
        self.assertTrue(np.all(velocity > 0.0))
        self.assertTrue(np.all(velocity < c))

        with self.assertRaises(ValueError):
            WaveguideSimulation(n_e=0.0, B=1.0, T_e=1.0e5)


if __name__ == "__main__":
    unittest.main()
