def replace_blank(str):
    """字符串中空格替换为指定字符"""
    if str is None:
        return
    original_length = len(str)
    number_of_blank = str.count(' ')
    new_length = original_length + number_of_blank * 2
    str_list = list(str)
    str_list.extend(['0' for _ in range(number_of_blank * 2)])
    index_of_original = original_length - 1
    index_of_new = new_length - 1
    while index_of_new != index_of_original:
        if str_list[index_of_original] == ' ':
            str_list[index_of_new] = '0'
            str_list[index_of_new-1] = '2'
            str_list[index_of_new-2] = '%'
            index_of_new = index_of_new - 3
        else:
            str_list[index_of_new] = str_list[index_of_original]
            index_of_new = index_of_new - 1

        index_of_original -= 1

    str = ''.join(str_list)
    print(str)


def match(s, pattern):
    """
    正则表达式匹配函数，注意这里[]不是None，但是len为0
    :param s: 字符串
    :param pattern: 模式
    :return: 是否匹配
    """
    # 字符串s长度和模式pattern长度均为0
    if len(s) == 0 and len(pattern) == 0:
        return True

    # 字符串s长度不为零,模式pattern长度为0
    elif len(s) != 0 and len(pattern) == 0:
        return False

    # 字符串s长度为零,模式pattern不为0
    elif len(s) == 0 and len(pattern) != 0:
        if len(pattern) > 1 and pattern[1] == '*':
            return match(s, pattern[2:])
        else:
            return False

    # 字符串s长度不为零,模式pattern长度不为0
    else:
        # 模式pattern长度大于1并且第二个元素为*
        if len(pattern) > 1 and pattern[1] == '*':
            # 字符串与模式第一个元素不同，则pattern前两位当成空
            if s[0] != pattern[0] and pattern[0] != '.':
                return match(s, pattern[2:])

            # 如果s[0]和pattern[0]相同，且pattern[1]为*，则
            # pattern后移两位，s不变，相当于置空pattern前两位，匹配后续
            # pattern后移两位，s后移一位，相当于pattern前两位与s[0]匹配
            # pattern不变，s后移一位，相当于pattern与s中的多位匹配
            # 第二种是第三种递归的结束条件
            else:
                return match(s, pattern[2:]) or \
                       match(s[1:], pattern[2:]) or \
                       match(s[1:], pattern)

        # 模式pattern长度为1或者模式第二个元素不为*
        else:
            # 如果相同或者匹配.，则继续判断
            if s[0] == pattern[0] or pattern[0] == '.':
                return match(s[1:], pattern[1:])
            # 不匹配
            else:
                return False


def is_numeric(string):
    """表示数值的字符串"""
    if len(string) == 0:
        return False

    numeric = scan_integer()
    if

def scan_unsigned_integer(string):
    for char in string:
        if char >= '9' or char <= '0':
            return False
    return True


def scan_integer(string):
    if string[0] == '+' or string[0] == '-':
        return scan_unsigned_integer(string[1:])
    return scan_unsigned_integer()


if __name__ == '__main__':
    # str = " faj kldaf ljf@$#@3 43 "
    # str = "fad"
    # replace_blank(str)
    print(match("abab", ".*b.."))
