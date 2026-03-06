import unittest

from color_conversion import convert_bt709_to_bt601


class TestBt709ToBt601(unittest.TestCase):
    def test_neutral_gray_stays_neutral(self) -> None:
        y, cb, cr = convert_bt709_to_bt601(128, 128, 128)
        self.assertEqual((y, cb, cr), (128, 128, 128))

    def test_known_color_pixel(self) -> None:
        # Reference value from direct matrix-chain computation.
        y, cb, cr = convert_bt709_to_bt601(100, 150, 200)
        self.assertEqual((y, cb, cr), (116, 142, 197))

    def test_10bit_limited_supported(self) -> None:
        y, cb, cr = convert_bt709_to_bt601(
            400, 512, 700, bit_depth=10, range_mode="limited"
        )
        self.assertTrue(0 <= y <= 1023)
        self.assertTrue(0 <= cb <= 1023)
        self.assertTrue(0 <= cr <= 1023)

    def test_full_range_supported(self) -> None:
        y, cb, cr = convert_bt709_to_bt601(100, 140, 220, range_mode="full")
        self.assertTrue(0 <= y <= 255)
        self.assertTrue(0 <= cb <= 255)
        self.assertTrue(0 <= cr <= 255)

    def test_invalid_range_raises(self) -> None:
        with self.assertRaises(ValueError):
            convert_bt709_to_bt601(100, 150, 200, range_mode="tv")


if __name__ == "__main__":
    unittest.main()
