# -*- coding: utf-8 -*-


class Node(object):
    """链表结点类,默认指针为零，即不存在下个结点"""
    def __init__(self, value, pointer=0):
        """初始化结点"""
        self.data = value
        self.next = pointer


class LinkedList(object):
    """链表类"""
    def __init__(self):
        """初始化链表"""
        self.head = 0   # 链表头指针

    def is_empty(self):
        """检查链表是否为空"""
        if self.head == 0:
            return True
        else:
            return False

    def print(self):
        if self.is_empty():
            print("Linked list is empty!")
        else:
            p = self.head
            while p != 0:
                print(p.data, p.next)
                p = p.next

    def length(self):
        """计算链表中结点个数"""
        length = 0
        p = self.head   # 提取头指针值
        while p != 0:
            length += 1
            p = p.next

        return length

    def clear(self):
        """清空链表"""
        self.head = 0

    def getitem(self, index):
        """获取链表中第index个节点，从0开始"""
        if self.is_empty():
            print("Linked list is empty!")
        else:
            j = 0
            p = self.head  # 提取头指针值
            while p.next != 0 and j < index:  # 寻找第index个结点
                j += 1
                p = p.next

            if j == index:  # 到达寻找结点
                return p.data
            else:
                print("Index exceeded!")

    def find(self, value):
        """寻找到链表中第一个等于某值的索引"""
        if self.is_empty():
            print("Link list if empty!")
        else:
            index = 0
            p = self.head
            while p.next != 0 and p.data != value:
                index += 1
                p = p.next

            if p.data == value:
                return index
            else:
                print("The given value was not found!")

    def init(self, data):
        """根据数组初始化链表"""
        if not self.is_empty():     # 链表非空，无法初始化
            print("Linked list isn't empty!")
        if data:
            self.head = Node(data[0])   # 设置链表首个结点，用于赋值head
            p = self.head   # 提取头指针值
            for i in data[1:]:
                node = Node(i)
                p.next = node
                p = p.next

    def append(self, item):
        """在链表尾部插入元素"""
        q = Node(item)
        if self.is_empty():  # 链表空
            self.head = q
        else:   # 链表非空
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q

    def insert(self, index, item):
        """在第index个位置上插入节点"""
        if self.is_empty():
            print("Link list if empty!")
        else:
            if index < 0:
                print("Index value cannot be negative!")
            elif index == 0:  # 插到头指针位置
                q = Node(item, self.head)   # 生成新的结点，并将地址指向原头指针
                self.head = q   # 更新头指针
            else:
                j = 0
                post = self.head
                p = self.head
                while p.next != 0 and j < index:
                    j += 1
                    post = p    # 标记前一个结点
                    p = p.next  # 标记下一个结点
                if index == j:
                    q = Node(item, p)
                    post.next = q
                else:
                    print("Index exceeded!")

    def delete(self, index):
        """删除第index个节点"""
        if self.is_empty():
            print("Link list if empty!")
        else:
            if index < 0:
                print("Index value cannot be negative!")
            elif index == 0:  # 删除头指针位置
                self.head = self.head.next  # 更新头指针
            else:
                j = 0
                p = self.head
                post = self.head
                while p.next != 0 and j < index:
                    j += 1
                    post = p    # 第j个节点
                    p = p.next  # 标记下一个结点
                if index == j:
                    post.next = p.next
                else:
                    print("Index exceeded!")


if __name__ == '__main__':
    linkedlist = LinkedList()   # 生成空链表
    linkedlist.print()   # 打印
    linkedlist.init([1, 2, 3, 4, 5])     # 链表初始化
    linkedlist.print()   # 打印
    print(linkedlist.getitem(4))
    linkedlist.append(6)
    print(linkedlist.find(3))
    # linkedlist.insert(5, 5)
    # linkedlist.print()   # 打印
    linkedlist.delete(1)
    linkedlist.print()   # 打印

