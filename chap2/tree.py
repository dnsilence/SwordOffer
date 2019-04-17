# -*- coding: utf-8 -*-


class Tree(object):
    """二叉树类"""
    def __init__(self, root=None, left=None, right=None):
        """初始化"""
        self.root = root
        self.left = left
        self.right = right

    def __pre_order(self, tree):
        """前序遍历内部函数"""
        if tree is not None:
            print(tree.root)
            self.__pre_order(tree.left)
            self.__pre_order(tree.right)

    def pre_order(self):
        """实现前序遍历，因为递归传入有可能为空，这里没有采用设定默认值判断为空
        的方式设置类方法，而是采用两个函数，以下遍历方法同理"""
        print("Pre order:")
        self.__pre_order(self)

    def __in_order(self, tree):
        """中序遍历内部函数"""
        if tree is not None:
            self.__in_order(tree.left)
            print(tree.root)
            self.__in_order(tree.right)

    def in_order(self):
        """实现中序遍历"""
        print("In order:")
        self.__in_order(self)

    def __post_order(self, tree):
        """后序遍历内部函数"""
        if tree is not None:
            self.__post_order(tree.left)
            self.__post_order(tree.right)
            print(tree.root)

    def post_order(self):
        """实现后序遍历"""
        print("Post order:")
        self.__post_order(self)


if __name__ == '__main__':
    tree = Tree('D',
                Tree('B',
                     Tree('A'),
                     Tree('C')
                     ),
                Tree('E',
                     None,
                     Tree('G',
                          Tree('F')
                          )
                     )
                )

    tree.pre_order()
    tree.in_order()
    tree.post_order()
