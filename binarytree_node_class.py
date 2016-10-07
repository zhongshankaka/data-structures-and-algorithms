# -*- coding: utf-8 -*-


class BiTNodeError(ValueError):
    pass


class BiTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def count_bitnodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_bitnodes(t.left) + count_bitnodes(t.right)

def sum_bitnodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_bitnodes(t.left) + sum_bitnodes(t.right)

def preorder(t, proc): #proc为具体的结点data操作
    if t is None:
        return
    assert(isinstance(t, BiTNode))
    proc(t.data)
    preorder(t.left)
    preorder(t.right)

def inorder(t, proc):
    if t is None:
        return
    inorder(t.left)
    proc(t.data)
    inorder(t.right)

def postorder(t, proc):
    if t is None:
        return
    postorder(t.left)
    postorder(t.right)
    proc(t.data)


# 深度优先遍历

from stack_class import *

def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            proc(t.data)
            t = t.left
        t = s.pop()

def preorder_iter(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()

def inorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right

def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            if t.left:
                t = t.left
            else:
                t = t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None



class BiTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root == None

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def preorder_iter(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()

