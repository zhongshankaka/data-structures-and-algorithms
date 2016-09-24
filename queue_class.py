# -*- coding: utf-8 -*-


class QueueUnderflow(ValueError):
    pass


class SQueue():
    def __init__(self, init_len=8):
        self.len = init_len
        self.elems = [0] * init_len
        self.head = 0
        self.num = 0

    def is_empty(self):
        return self.num == 0

    def peek(self):
        if self.num == 0:
            raise QueueUnderflow
        return self.elems[self.head]

    def dequeue(self):
        if self.num == 0:
            raise QueueUnderflow
        e = self.elems[self.head]
        self.head = (self.head+1) % self.len
        self.num -= 1
        return e

    def enqueue(self, elem):
        if self.num == self.len:
            self._extend()
        self.elems[(self.head+self.num) % self.len] = elem
        self.num += 1

    def _extend(self):
        old_len = self.len
        self.len *= 2
        new_elems = [0]*(self.len)
        for i in range(old_len):
            new_elems[i] = self.elems[(self.head+i) % old_len]
        self.elems, self.head = new_elems, 0
        