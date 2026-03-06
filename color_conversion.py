"""BT.709 <-> BT.601 Y'CbCr conversion utilities.

This module converts gamma-corrected Y'CbCr code values between BT.709 and
BT.601 by using R'G'B' as the intermediate domain.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Primaries:
    """Luma coefficients for Y' = Kr*R' + Kg*G' + Kb*B'."""

    kr: float
    kb: float

    @property
    def kg(self) -> float:
        return 1.0 - self.kr - self.kb


BT709 = Primaries(kr=0.2126, kb=0.0722)
BT601 = Primaries(kr=0.2990, kb=0.1140)


def _range_params(bit_depth: int, range_mode: str) -> Tuple[float, float, float, float]:
    if bit_depth < 8:
        raise ValueError("bit_depth must be >= 8")
    if range_mode not in {"limited", "full"}:
        raise ValueError("range_mode must be one of: limited, full")

    scale = 1 << (bit_depth - 8)
    maxv = float((1 << bit_depth) - 1)
    if range_mode == "limited":
        y_offset = float(16 * scale)
        y_scale = float(219 * scale)
        c_offset = float(128 * scale)
        c_scale = float(224 * scale)
    else:
        y_offset = 0.0
        y_scale = maxv
        c_offset = maxv / 2.0
        c_scale = maxv
    return y_offset, y_scale, c_offset, c_scale


def _clip(value: float, low: float, high: float) -> float:
    return max(low, min(value, high))


def _decode_ycbcr(
    y_code: float, cb_code: float, cr_code: float, bit_depth: int, range_mode: str
) -> Tuple[float, float, float]:
    """Decode digital Y'CbCr code values to normalized Y' and centered Cb/Cr."""
    y_offset, y_scale, c_offset, c_scale = _range_params(bit_depth, range_mode)
    y = (y_code - y_offset) / y_scale
    cb = (cb_code - c_offset) / c_scale
    cr = (cr_code - c_offset) / c_scale
    return y, cb, cr


def _encode_ycbcr(
    y: float, cb: float, cr: float, bit_depth: int, range_mode: str
) -> Tuple[int, int, int]:
    """Encode normalized Y' and centered Cb/Cr to digital code values."""
    y_offset, y_scale, c_offset, c_scale = _range_params(bit_depth, range_mode)
    maxv = float((1 << bit_depth) - 1)

    y_code = y * y_scale + y_offset
    cb_code = cb * c_scale + c_offset
    cr_code = cr * c_scale + c_offset

    y_code = int(round(_clip(y_code, 0.0, maxv)))
    cb_code = int(round(_clip(cb_code, 0.0, maxv)))
    cr_code = int(round(_clip(cr_code, 0.0, maxv)))
    return y_code, cb_code, cr_code


def _ycbcr_to_rgb(
    y: float, cb: float, cr: float, primaries: Primaries
) -> Tuple[float, float, float]:
    """Convert normalized Y'CbCr to R'G'B'."""
    kr, kg, kb = primaries.kr, primaries.kg, primaries.kb

    r = y + 2.0 * (1.0 - kr) * cr
    b = y + 2.0 * (1.0 - kb) * cb
    g = (y - kr * r - kb * b) / kg
    return r, g, b


def _rgb_to_ycbcr(
    r: float, g: float, b: float, primaries: Primaries
) -> Tuple[float, float, float]:
    """Convert R'G'B' to normalized Y'CbCr."""
    kr, kg, kb = primaries.kr, primaries.kg, primaries.kb
    y = kr * r + kg * g + kb * b
    cb = (b - y) / (2.0 * (1.0 - kb))
    cr = (r - y) / (2.0 * (1.0 - kr))
    return y, cb, cr


def convert_bt709_to_bt601(
    y_code: float,
    cb_code: float,
    cr_code: float,
    *,
    bit_depth: int = 8,
    range_mode: str = "limited",
) -> Tuple[int, int, int]:
    """Convert one Y'CbCr pixel from BT.709 matrix to BT.601 matrix.

    Args:
        y_code: Y' code value.
        cb_code: Cb code value.
        cr_code: Cr code value.
        bit_depth: Bit depth of code values, e.g. 8 or 10.
        range_mode: "limited" (TV range) or "full".

    Returns:
        (Y', Cb, Cr) code values in BT.601.
    """
    y, cb, cr = _decode_ycbcr(y_code, cb_code, cr_code, bit_depth, range_mode)
    r, g, b = _ycbcr_to_rgb(y, cb, cr, BT709)
    y_601, cb_601, cr_601 = _rgb_to_ycbcr(r, g, b, BT601)
    return _encode_ycbcr(y_601, cb_601, cr_601, bit_depth, range_mode)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert one Y'CbCr pixel from BT.709 to BT.601."
    )
    parser.add_argument("--y", type=float, required=True, help="Input Y' code value")
    parser.add_argument("--cb", type=float, required=True, help="Input Cb code value")
    parser.add_argument("--cr", type=float, required=True, help="Input Cr code value")
    parser.add_argument(
        "--bit-depth", type=int, default=8, help="Code bit depth (default: 8)"
    )
    parser.add_argument(
        "--range-mode",
        choices=["limited", "full"],
        default="limited",
        help="Code range mode (default: limited)",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    y, cb, cr = convert_bt709_to_bt601(
        args.y, args.cb, args.cr, bit_depth=args.bit_depth, range_mode=args.range_mode
    )
    print(f"{y},{cb},{cr}")


if __name__ == "__main__":
    main()
