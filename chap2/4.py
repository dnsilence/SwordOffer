# -*- coding:utf-8 -*-


def find(matrix, number):
    if matrix is not None:
        rows = len(matrix)
        columns = len(matrix[0])
        # 从右上角开始查询
        row = 0               # 从第0行开始
        column = columns - 1  # 从第column-1列开始
        while row <= (rows-1) and column >= 0:
            if matrix[row][column] < number:       # 当前值小于寻找值
                row += 1  # 往下找
            elif matrix[row][column] > number:     # 当前值大于寻找值
                column -= 1  # 往左找
            else:
                return True, [row, column]
    return False, [0, 0]


if __name__ == '__main__':
    # matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 7, 10]]
    matrix = [[]]
    a, b = find(matrix, 19)
    print(a, b)
