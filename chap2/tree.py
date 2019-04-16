# -*- coding: utf-8 -*-


class Tree(object):
    """二叉树类"""
    def __init__(self, root=None, left=None, right=None):
        """初始化"""
        self.root = root
        self.left = left
        self.right = right


def pre_order(tree):
    if tree.root is not None:
        print(tree.root)
        pre_order(tree.left)
        pre_order(tree.right)