# -*- coding:utf-8 -*-


def duplicate(numbers, duplication):
    """查找数组中重复的元素"""
    # 输入检查
    if numbers is None or len(numbers) <= 1:
        return False
    for i in range(len(numbers)):
        if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
            return False
    # # 排序查找
    # numbers.sort()
    # for i in range(len(numbers) - 1):
    #     if numbers[i] == numbers[i + 1]:
    #         duplication[0] = numbers[i]
    #         return True

    # 交换查找
    for i in range(len(numbers)):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                duplication[0] = numbers[i]
                return True
            # # 这里必须将索引提取
            # idx = numbers[i]
            # numbers[i], numbers[idx] = numbers[idx], numbers[i]
            # 这种方式也可以，
            numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
            # # 这种方式不可以，
            # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
    return False


def find(matrix, number):
    """查找二维数组中某个元素"""
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
    # 查找数组中重复的元素
    # numbers = [2, 3, 1, 0, 2, 5, 3]     # 数组中包含一个或多个重复数字
    numbers = []     # 无效输入
    numbers = [1, 2, 3, 4, 5, 6]    # 不包括重复数字
    duplication = [0]
    print(duplicate(numbers, duplication), duplication[0])

    # 查找二维数组中某一元素
    # matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 7, 10]]
    matrix = [[]]
    a, b = find(matrix, 19)
    print(a, b)

