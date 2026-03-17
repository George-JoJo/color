"""Color space conversion utilities."""

from __future__ import annotations

import numpy as np


# Common CIE standard illuminant D65 white point (2° observer).
D65_WHITEPOINT = np.array([0.95047, 1.0, 1.08883], dtype=float)


def xyz_to_lab(xyz, whitepoint=D65_WHITEPOINT):
    """
    将XYZ值转换为Lab色彩空间
    :param xyz: XYZ值数组, 形状为(3,)或(n,3)
    :param whitepoint: 参考白点, 默认为D65
    :return: Lab值数组
    """
    # 确保输入为numpy数组
    xyz = np.asarray(xyz, dtype=float)
    if xyz.ndim == 1:
        if xyz.shape[0] != 3:
            raise ValueError("xyz must have shape (3,) or (n, 3)")
        xyz = xyz[np.newaxis, :]
    elif xyz.ndim == 2:
        if xyz.shape[1] != 3:
            raise ValueError("xyz must have shape (3,) or (n, 3)")
    else:
        raise ValueError("xyz must have shape (3,) or (n, 3)")

    whitepoint = np.asarray(whitepoint, dtype=float)
    if whitepoint.shape != (3,):
        raise ValueError("whitepoint must have shape (3,)")

    # 归一化到白点
    xyz_norm = xyz / whitepoint

    # 非线性变换
    epsilon = 216 / 24389  # (6/29)^3
    kappa = 24389 / 27  # (29/3)^3

    f = np.where(
        xyz_norm > epsilon,
        np.cbrt(xyz_norm),
        (kappa * xyz_norm + 16) / 116,
    )

    # 计算Lab值
    L = 116 * f[:, 1] - 16
    a = 500 * (f[:, 0] - f[:, 1])
    b = 200 * (f[:, 1] - f[:, 2])

    # 返回结果
    lab = np.column_stack((L, a, b))
    return lab.squeeze()

