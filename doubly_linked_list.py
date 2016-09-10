from single_linked_list import LNode, LList1

class DLNode(LNode):
    def __init__(self, prev, elem, nxt):
        LNode.__init__(self, elem, nxt)
        self.prev = prev

class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(None, elem, self._head)
        self._head = p
        if self._rear is None:
            self._rear = p
        else:
            p.next.prev = p

    def append(self, elem):
        p = DLNode(self._rear, elem, None)
        self._rear = p
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p

    def pop(self):
        if self._head is None:
            raise ValueError
        e = self._head.elem
        self._head = self._head.next
        if self._head is None:
            self._rear = None
        else:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise ValueError
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e


if __name__ == '__main__':
    mlist = DLList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    #mlist1.printall()

    while not mlist.isEmpty():
        print(mlist.pop())
        if not mlist.isEmpty():
            print(mlist.poplast())