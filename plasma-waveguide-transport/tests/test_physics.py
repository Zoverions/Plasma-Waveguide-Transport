import sys
import os
import unittest
import numpy as np
from scipy.constants import c

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from plasma_physics import plasma_frequencies, whistler_group_velocity

class TestPlasmaPhysics(unittest.TestCase):
    def test_plasma_frequencies(self):
        n_e = 1e18
        B = 1.0
        wp, wc = plasma_frequencies(n_e, B)
        self.assertGreater(wp, 0)
        self.assertGreater(wc, 0)

    def test_whistler_group_velocity(self):
        n_e = 1e18
        B = 1.0
        omega = 2 * np.pi * 1e9 # 1 GHz
        vg = whistler_group_velocity(omega, n_e, B)
        self.assertGreater(vg, 0)
        # Check subluminal
        self.assertLess(vg, c)

    def test_group_velocity_vectorized(self):
        n_e = 1e18
        B = 1.0
        omegas = np.array([1e9, 2e9, 3e9])
        vg = whistler_group_velocity(omegas, n_e, B)
        self.assertEqual(len(vg), 3)
        self.assertTrue(np.all(vg < c))

if __name__ == '__main__':
    unittest.main()
