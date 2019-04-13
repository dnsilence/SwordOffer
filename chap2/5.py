# -*- coding:utf-8 -*-


def replace_blank(str):
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


if __name__ == '__main__':
    # str = " faj kldaf ljf@$#@3 43 "
    str = "fad"
    replace_blank(str)
