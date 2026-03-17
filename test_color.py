import unittest

import numpy as np

from color import D65_WHITEPOINT, xyz_to_lab


class XyzToLabTests(unittest.TestCase):
    def test_whitepoint_maps_to_neutral_100(self):
        lab = xyz_to_lab(D65_WHITEPOINT)
        np.testing.assert_allclose(lab, np.array([100.0, 0.0, 0.0]), atol=1e-6)

    def test_black_maps_to_zero(self):
        lab = xyz_to_lab(np.array([0.0, 0.0, 0.0]))
        np.testing.assert_allclose(lab, np.array([0.0, 0.0, 0.0]), atol=1e-6)

    def test_batch_input(self):
        xyz = np.array(
            [
                D65_WHITEPOINT,
                [0.0, 0.0, 0.0],
            ]
        )
        lab = xyz_to_lab(xyz)
        expected = np.array(
            [
                [100.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ]
        )
        np.testing.assert_allclose(lab, expected, atol=1e-6)


if __name__ == "__main__":
    unittest.main()

