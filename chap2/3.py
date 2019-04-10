# -*- coding:utf-8 -*-


def duplicate(numbers, duplication):
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


if __name__ == '__main__':
    # numbers = [2, 3, 1, 0, 2, 5, 3]     # 数组中包含一个或多个重复数字
    numbers = []     # 无效输入
    numbers = [1, 2, 3, 4, 5, 6]    # 不包括重复数字
    duplication = [0]
    print(duplicate(numbers, duplication), duplication[0])

