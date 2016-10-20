# -*- coding: utf-8 -*-


def insert_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        for j in range(i, -1, -1):
            if lst[j-1].key > x.key:
                lst[j] = lst[j-1]
            else:
                break
        lst[j] = x


def select_sort(lst):
    for i in range(len(lst)-1):
        k = i
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]


def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst)-i):
            if lst[j-1].key > lst[j].key:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:
            break


def quick_sort(lst):
    qsort_rec(lst, 0, len(lst)-1)

def qsort_rec(lst, l, r):
    if l >= r:
        return
    i = l
    j = r
    pivot = lst[i]
    while i < j:
        while i < j and lst[j].key >= pivot.key:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i].key <= pivot.key:
            i += 1
        if i < j:
            lst[j] = lst[i]
            j -= 1
        lst[i] = pivot


# 归并排序
def merge(from_lst, to_lst, low, m, high):
    i, j, k = low, m+1, low
    while i < m and j < high:
        if from_lst[i].key <= from_lst[j].key:
            to_lst[k] = from_lst[i]
            i += 1
        else:
            to_lst[k] = from_lst[j]
            j += 1
        k += 1
    while i <= m:
        to_lst[k] = from_lst[i]
        i += 1
        k += 1
    while j <= high:
        to_lst[k] = from_lst[j]
        j += 1
        k += 1

def merge_pass(from_lst, to_lst, llen, slen):
    i = 1
    while i + 2*slen - 1 <= llen:
        merge(from_lst, to_lst, i, i+slen-1, i+2*slen-1)
        i += 2*slen
    if i + slen - 1 < llen:
        merge(from_lst, to_lst, i, i +slen-1, llen)
    else:
        for j in range(i, llen):
            to_lst[j] = from_lst[j]

def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None for i in range(llen)]
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2