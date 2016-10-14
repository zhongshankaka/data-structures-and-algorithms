# -*- coding: utf-8 -*-


class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __str__(self):
        return "Assoc({0}, {1}".format(self.key, self.value)


# 二分搜索

def bisearch(lst, key):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low+high)//2
        if key == lst[mid].key:
            return lst[mid].value
        if key < lst[mid].key:
            high = mid - 1
        else:
            low = mid + 1

# 哈希表

