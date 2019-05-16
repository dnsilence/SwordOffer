# -*- coding:utf-8 -*-
import math


def cut_rope(length):
    """动态规划求最大值"""
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    times_of_3 = length // 3

    if length - times_of_3 * 3 == 1:
        times_of_3 -= 1
    # 这里肯定可以整除，但为了后面乘方为整数，选择使用//
    times_of_2 = (length - times_of_3 * 3) // 2

    return 3**times_of_3*2**times_of_2


if __name__ == '__main__':
    print(cut_rope(0))
    print(cut_rope(1))
    print(cut_rope(2))
    print(cut_rope(3))
    print(cut_rope(4))
    print(cut_rope(5))
    print(cut_rope(6))
