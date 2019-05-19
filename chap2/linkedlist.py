# -*- coding: utf-8 -*-


class Node(object):
    """链表结点类,默认指针不存在下个结点"""
    def __init__(self, value, pointer=None):
        """初始化结点"""
        self.data = value
        self.next = pointer


class LinkedList(object):
    """链表类"""
    def __init__(self):
        """初始化链表"""
        self.head = None   # 链表头指针

    def is_empty(self):
        """检查链表是否为空"""
        if self.head is None:
            return True
        else:
            return False

    def print(self):
        if self.is_empty():
            print("Linked list is empty!")
        else:
            p = self.head
            while p is not None:
                print(p.data, p.next)
                p = p.next

    def print_reverse(self, head=None):
        """链表反转打印"""
        if not head:    # 传入，注意这里的赋值，必须放前面
            head = self.head
        if head:
            # 使用递归实现倒序打印
            # if head is not None:  # 如果当前传入指针非空
            if head.next:
                self.print_reverse(head.next)
            print(head.data)  # 打印当前结点数据

    def length(self):
        """计算链表中结点个数"""
        length = 0
        pointer = self.head   # 提取头指针值
        while pointer:
            length += 1
            pointer = pointer.next
        return length

    def clear(self):
        """清空链表"""
        self.head = None

    def getitem(self, index):
        """获取链表中第index个节点，从0开始"""
        if self.is_empty():
            print("Linked list is empty!")
        else:
            j = 0
            p = self.head  # 提取头指针值
            while p.next and j < index:  # 寻找第index个结点
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
            while p.next and p.data != value:
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
            while p.next:
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
                while p.next and j < index:
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
                while p.next and j < index:
                    j += 1
                    post = p    # 第j个节点
                    p = p.next  # 标记下一个结点
                if index == j:
                    post.next = p.next
                else:
                    print("Index exceeded!")


def delete_duplication(p_head):
    """删除一个排序链表中重复的节点"""
    if p_head is None or p_head.next is None:
        # 传入为空或只有一个元素
        return p_head
    first = Node(-1)    # 生成一个临时节点，头指针为first，删除头结点时有用
    first.next = p_head     # 临时节点指向传入指针头结点
    last = first    # 生成一个指针用于指向重复值的上一个结点
    while p_head and p_head.next:   # 如果当前头指针不为空且下一个也不为空
        # 因为p_head发生移动，所以必须检查当前是否为零，
        # p_head.next若为空，则后面不会有重复值
        if p_head.data == p_head.next.data:   # 如果当前节点的和下一节点值相同
            val = p_head.data    # 提取重复值
            while p_head and val == p_head.data:     # 没有下一个节点或者值不相等
                p_head = p_head.next    # 移动指针，可能使得p_head为空
            last.next = p_head      # 通过更新last的下一个值删除掉重复结点
        else:   # 否则
            last = p_head   # 更新当前节点到last
            p_head = p_head.next    # 移动指针
    return first.next


def print_linkedlist(p_head):
    if p_head is None:
        print("Linked list is empty!")
    else:
        while p_head:
            print(p_head.data)
            p_head = p_head.next


if __name__ == '__main__':
    linkedlist = LinkedList()   # 生成空链表
    # linkedlist.print()   # 打印
    # linkedlist.init([1, 2, 3, 4, 5])     # 链表初始化
    linkedlist.init([1, 1, 1, 1, 1])     # 链表初始化
    # linkedlist.init([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])     # 链表初始化
    # linkedlist.print()   # 打印
    # linkedlist.print_reverse()
    print_linkedlist(delete_duplication(linkedlist.head))
    # print(linkedlist.getitem(4))
    # linkedlist.append(6)
    # print(linkedlist.find(3))
    # # linkedlist.insert(5, 5)
    # # linkedlist.print()   # 打印
    # linkedlist.delete(1)
    # linkedlist.print()   # 打印

