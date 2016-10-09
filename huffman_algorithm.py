# -*- coding: utf-8 -*-

from priority_queue import PrioQueueError, PrioQueue
from binarytree_node_class import BiTNode, print_BiTNodes


class HTNode(BiTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data


class HuffmanPrioQ(PrioQueue):
    def number(self):
        return self.num


def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w, None, None))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()


if __name__ == "__main__":
    h = HuffmanTree([2, 3, 7, 10, 4, 2, 5])
    print_BiTNodes(h)