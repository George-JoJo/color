#!/usr/bin/env python3

from __future__ import annotations


def selection_sort(items: list[int]) -> list[int]:
    """Return a new list sorted in ascending order.

    This implementation assumes the input contains exactly 30 elements.
    """
    if len(items) != 30:
        raise ValueError("输入数组必须包含 30 个元素。")

    result = items[:]
    n = len(result)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]
    return result


def main() -> None:
    # 示例：包含 30 个元素的数组
    data = [
        42, 7, 19, 88, 3, 65, 14, 27, 9, 71,
        56, 2, 33, 90, 12, 48, 6, 73, 21, 38,
        81, 5, 60, 29, 17, 95, 24, 11, 67, 1,
    ]
    print("原始数组:", data)
    print("排序结果:", selection_sort(data))


if __name__ == "__main__":
    main()
