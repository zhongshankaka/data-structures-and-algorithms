# -*- coding: utf-8 -*-

from binarytree_node_class import BiTNode, print_BiTNodes
from stack_class import SStack
from dict_class import Assoc


# 二叉排序树的实现
# 检索算法
def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None


# 二叉排序树字典类
class DictBTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def preorder(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()

    def inorder(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data
            t = t.right

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BiTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BiTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BiTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
            return

    def delete(self, key):
        p, q = None, self._root
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
        if q is None:
            return
        if q.left is None:
            if p is None:
                self._root = q.right
            elif q == p.left:
                p.left = q.right
            else:
                p.right = q.right
            return
        r = q.left
        while r.right is not None:
            r = r.right
        r.right = q.right
        if p == None:
            self._root = q.left
        elif p.left == q:
            p.left = q.left
        else:
            p.right = q.left

    def print(self):
        for entry in self.inorder():
            print(entry.key, entry.value)


def build_dictBT(entries):
    dic = DictBTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic


# if __name__ == '__main__':
#     from random import randint
#
#     data = [(x, 1) for x in
#             [36, 65, 18, 7, 60, 89, 43, 57, 101, 52, 74]]
#     dic1 = build_dictBT(data)
#
#     for entry in dic1.inorder():
#         print(entry.key, entry.value)
#
#     pass


# 最佳二叉排序树

from dict_class import Assoc

inf = float("inf")

class DictOptBTree(DictBTree):
    def __init__(self, seq):
        DictBTree.__init__(self)
        data = sorted(seq)
        self._root = DictOptBTree.buildOBT(data, 0, len(data)-1)

    @staticmethod
    def buildOBT(data, start, end):
        if start > end:
            return None
        mid = (end+start)//2
        left = DictOptBTree.buildOBT(data, start, mid-1)
        right = DictOptBTree.buildOBT(data, mid+1, end)
        return BiTNode(Assoc(*data[mid]), left, right)


def build_opt_btree(wp, wq): # wp为内部结点序列，wq为外部结点序列
    num = len(wp) + 1
    if len(wq) != num:
        raise ValueError("Arguments of build_opt_btree are wrong.")
    w = [[0 for i in range(num)] for j in range(num)]
    c = [[0 for i in range(num)] for j in range(num)]
    r = [[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        w[i][i] = wq[i]
        for j in range(i + 1, num):
            w[i][j] = w[i][j - 1] + wp[j - 1] + wq[j]
    for i in range(0, num - 1):
        c[i][i + 1] = w[i][i + 1]
        r[i][i + 1] = i

    for m in range(2, num):

        for i in range(0, num - m):
            k0, j = i, i + m
            wmin = inf
            for k in range(i, j):
                if c[i][k] + c[k + 1][j] < wmin:
                    wmin = c[i][k] + c[k + 1][j]
                    k0 = k
            c[i][j] = w[i][j] + wmin
            r[i][j] = k0

    return (c, r)


# if __name__ == '__main__':
#     from random import randint
#
#     wp = [5, 1, 2]
#     wq = [4, 3, 1, 1]
#
#     trees = build_opt_btree(wp, wq)
#
#     print(trees[0])
#     print(trees[1])
#
#     wp = [5, 1, 2, 6, 8, 10]
#     wq = [4, 3, 3, 1, 6, 12, 9]
#
#     trees = build_opt_btree(wp, wq)
#
#     print(trees[0])
#     print(trees[1])
#
#     ##    "Result:"
#     ##    [[0, 12, 23, 35, 66, 112, 167],
#     ##     [0,  0,  7, 16, 38,  80, 130],
#     ##     [0,  0,  0,  6, 24,  62, 112],
#     ##     [0,  0,  0,  0, 13,  46,  96],
#     ##     [0,  0,  0,  0,  0,  26,  71],
#     ##     [0,  0,  0,  0,  0,   0,  31],
#     ##     [0,  0,  0,  0,  0,   0,   0]]
#     ##
#     ##    [[0, 0, 0, 0, 3, 3, 4],
#     ##     [0, 0, 1, 1, 3, 4, 4],
#     ##     [0, 0, 0, 2, 3, 4, 4],
#     ##     [0, 0, 0, 0, 3, 4, 4],
#     ##     [0, 0, 0, 0, 0, 4, 5],
#     ##     [0, 0, 0, 0, 0, 0, 5],
#     ##     [0, 0, 0, 0, 0, 0, 0]]


# 平衡二叉树

from stack_class import SStack
from binarytree_node_class import BiTNode, print_BiTNodes

class AVLNode(BiTNode):
    def __init__(self, data):
        BiTNode.__init__(self, data)
        self.bf = 0 #平衡因子

class DictAVL(DictBTree):
    def __init__(self):
        self._root = None

    @staticmethod
    def LL(a, b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def RR(a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        c = b.right
        a.left, c.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = -1
            b.bf = 0
        else:
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c
