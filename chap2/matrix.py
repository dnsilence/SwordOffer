# -*- coding:utf-8 -*-


def has_path(matrix, rows, cols, path):
    """
    二维矩阵中寻找是否存在指定路径
    :param matrix: 输入矩阵
    :param rows: 矩阵行数
    :param cols: 矩阵列数
    :param path: 待寻找路径
    :return:
    """
    # 输入合法性检查
    if matrix is None or rows < 1 or cols < 1 or len(path) == 0 \
            or len(matrix) != rows*cols:
        return False

    visited = [0]*(rows*cols)   # 辅助矩阵
    char_index = 0     # 寻找path中的第0个字母
    # 从左到右，从上到下遍历
    for row in range(rows):
        for col in range(cols):
            if has_path_core(matrix, rows, cols, row, col, path, char_index,
                             visited):
                return True
    return False


def has_path_core(matrix, rows, cols, row, col, path, char_index, visited):
    """
    寻找指定位置是否有某一值
    :param matrix:输入矩阵
    :param rows:矩阵行数
    :param cols:矩阵列数
    :param row:寻找位置
    :param col:寻找位置
    :param path:待寻找路径
    :param char_index:寻找路径中的第char_index个字母
    :param visited:访问状态矩阵
    :return:是否找到
    """
    if len(path) == char_index:    # 如果已经找到最后一个字母，返回
        return True

    has_path_flag = False    # 默认无路径标示

    if (0 <= row < rows and 0 <= col < cols and not visited[row*cols+col] and
            matrix[row*cols+col] == path[char_index]):
        """在索引值未超出矩阵范围，且之前未被访问的条件下找到当前位置为寻找值"""
        char_index += 1    # 寻找准备寻找下一个位置
        visited[row*cols+col] = True    # 将虚拟矩阵中的第row*cols+col个值标记为真
        # 寻找当前未知的相邻位置是否有指定元素，递归，直到找完所有
        has_path_flag = (has_path_core(matrix, rows, cols, row, col-1, path,
                                       char_index, visited) or
                         has_path_core(matrix, rows, cols, row, col+1, path,
                                       char_index, visited) or
                         has_path_core(matrix, rows, cols, row-1, col, path,
                                       char_index, visited) or
                         has_path_core(matrix, rows, cols, row+1, col, path,
                                       char_index, visited))
        if not has_path_flag:   # 如果没有找到，则需清除当前状态
            char_index -= 1    # 待寻找值减一
            visited[row*cols+col] = False   # 访问状态清除
    return has_path_flag


if __name__ == '__main__':
    # a b t g
    # c f c s
    # j d e h
    matrix = ['a', 'b', 't', 'g', 'c', 'f', 'c', 's', 'j', 'd', 'e', 'h']
    # path = ['t', 'c', 'e']
    # path = ['b', 'f', 'c', 't']
    # path = []
    path = ['t', 'g', 'c']
    print(has_path(matrix, 12, 1, path))



