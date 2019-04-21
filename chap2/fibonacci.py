# -*- coding:utf-8 -*-


# def fibonacci(number):
#     """错误做法，采用递归"""
#     if number <= 0:
#         return 0
#     if number == 1:
#         return 1
#     return fibonacci(number - 1) + fibonacci(number - 2)


# def fibonacci(number):
#     """斐波那契数列循环解法"""
#     if number <= 0:
#         return 0
#     elif number == 1:
#         return 1
#     else:
#         back_1, back_2 = 1, 0
#         for _ in range(number - 1):
#             new_value = back_1 + back_2
#             back_2, back_1 = back_1, new_value
#         return new_value

def fibonacci(number):
    """采用求余寻找下标实现的循环"""
    if number <= 0:
        return 0
    temp_array = [0, 1]
    if number >= 2:
        for index in range(2, number+1):
            temp_array[index % 2] = temp_array[0] + temp_array[1]
    return temp_array[number % 2]


if __name__ == '__main__':
    print(fibonacci(-1))
    for i in range(10):
        print(fibonacci(i))


