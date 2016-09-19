# -*- coding: utf-8 -*-

#结点类模块

class LNode:
    def __init__(self, elem, next):
        self.elem = elem
        self.next = next

# if __name__ == '__main__':
#     llist1 = LNode(1, None)
#     pnode = llist1
#
#     for i in range(2, 11):
#         pnode.next = LNode(i, None)
#         pnode = pnode.next
#
#     pnode = llist1
#     while pnode != None:
#         print(pnode.elem)
#         pnode = pnode.next


#简单单链表模块

class LList:
    def __init__(self):
        self._head = None

    def isEmpty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise ValueError
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, None)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem, None)

    def pop_last(self):
        if self._head is None:
            raise ValueError
        p = self._head
        if p.next is None:
            e = p.elem
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem): #找到满足此条件的结点
                return p.elem
            p = p.next
        return None

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem)
            p = p.next

# if __name__ == '__main__':
#     mlist1 = LList()
#
#     for i in range(10):
#         mlist1.prepend(i)
#
#     for i in range(10):
#         mlist1.append(i)
#
#     mlist1.printall()


#带尾结点的单链表模块

class LList1(LList):
    def __init__(self):
        super(LList1, self).__init__()
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._rear is None:
            self.prepend(elem)
        else:
            self._rear.next = LNode(elem, None)
            self._rear = self._rear.next

    def pop(self):
        if self._head is None:
            raise ValueError
        e = self._head.elem
        if self._rear is self._head:
            self._rear = None
        self._head = self._head.next
        return e

    def pop_last(self):
        if self._head is None:
            raise ValueError
        p = self._head
        if p.next_ is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

# if __name__ == '__main__':
#     mlist1 = LList1()
#     for i in range(10):
#         mlist1.prepend(i)
#
#     for i in range(11, 20):
#         mlist1.append(i)
#
#     mlist1.printall()


#循环单链表模块

class LCList:
    def __init__(self):
        self._rear = None

    def isEmpty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem, None)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next #未插入p时的self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise ValueError
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

if __name__ == '__main__':
    mlist1 = LCList()

    for i in range(10):
        mlist1.prepend(i)

    for i in range(10):
        mlist1.append(i)

    mlist1.printall()


#带反转和排序的单链表模块

class LList:
    def __init__(self):
        self._head = None

    def isEmpty(self):
        return self.head is None

    def prepend(self, elem):
        self.head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise ValueError
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, None)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem, None)

    def  pop_last(self):
        if self._head is None:
            raise ValueError
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print('')

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort1(self): #移动表中元素
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x, p = crt.elem, self._head
            while p is not crt and p.elem <= x:
                p = p.next
                while p is not crt:
                    y = p.elem
                    p.elem = x
                    x = y
                    p = p.next
                crt.elem = x
                crt = crt.next

    def sort2(self): #调整结点之间的连接关系
        if self._head is None:
            return
        last = self._head
        crt = last.next
        while crt is not None:
            p = self._head
            q = None
            while p is not crt and p.elem <= crt.elem:
                q = p
                p = p.next
            if p is crt:
                last = crt
            else:
                last.next = crt.next
                crt.next = p
                if q is None:
                    self._head = crt
                else:
                    q.next = crt
            crt = last.next



if __name__ == '__main__':
    mlist1 = LList()

    for i in range(10):
        mlist1.prepend(i)

    for i in range(11, 20):
        mlist1.append(i)

    mlist1.printall()

    for i in range(5):
        print(mlist1.pop())
        print(mlist1.poplast())

    print('remained:')
    mlist1.printall()

    mlist1.rev()
    print('\nreversed:')
    mlist1.printall()

    mlist1.sort2()
    print('\nsorted:')
    mlist1.printall()



















