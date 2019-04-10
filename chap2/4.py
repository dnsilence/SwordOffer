# -*- coding:utf-8 -*-


def Find(matrix, number):
    if matrix is not None:
        row = len(matrix)
        column = len(matrix[0])
        # 从右上角开始查询
        i = 0               # 从第0行开始
        j = column - 1  # 从第column-1列开始
        while i <= (row-1) and j >= 0:
            if matrix[i][j] < number:       # 当前值小于寻找值
                i += 1  # 往下找
            elif matrix[i][j] > number:     # 当前值大于寻找值
                j -= 1  # 往左找
            else:
                return True, [i, j]
    return False, [0, 0]


if __name__ == '__main__':
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 7, 10]]
    a, b = Find(matrix, 19)
    print(a, b)
