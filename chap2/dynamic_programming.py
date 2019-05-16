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
    products = [0]*(length+1)
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    for i in range(4, length+1):
        """求解所有小的问题"""
        max = 0
        for j in range(1, math.floor(i/2)+1):
            product = products[j] * products[i-j]
            if max < product:
                max = product
            products[i] = max

    max = products[length]
    return max


if __name__ == '__main__':
    print(cut_rope(0))
    print(cut_rope(1))
    print(cut_rope(2))
    print(cut_rope(3))
    print(cut_rope(4))
    print(cut_rope(5))
    print(cut_rope(6))
