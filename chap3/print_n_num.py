def print_1_to_max_of_n_digits(number):
    """打印1到最大的number位数"""
    if number <= 0:
        return
    number_string = ['0'] * number
    for i in range(10):
        number_string[0] = str(i)   # 数组开始保存着最高位
        print_1_to_max_of_n_digits_recursively(number_string, number, 0)


def print_1_to_max_of_n_digits_recursively(number_string, length, index):
    if index == length-1:
        print_number(number_string)
        return
    for i in range(10):
        number_string[index+1] = str(i)
        print_1_to_max_of_n_digits_recursively(number_string, length, index+1)


def print_number(number_string):
    """
    输出一个
    :param number_string: str类型数组，每个元素是0-9数字的字符串形式
    :return: None
    """
    begin_flag = False  # 开始输出标志位
    length = len(number_string)
    for i in range(length):
        if not begin_flag and number_string[i] != '0':     # 只输出非零项
            begin_flag = True
        if begin_flag:
            print('%c' % number_string[i], end='')
    print('\t')


if __name__ == '__main__':
    print_1_to_max_of_n_digits(4)
