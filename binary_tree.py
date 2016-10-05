# -*- coding:utf-8 -*-

def BiTree(data, left, right):
    return [data, left, right]

def is_empty_BiTree(bitree):
    return bitree == []

def root(bitree):
    return bitree[0]

def left(bitree):
    return bitree[1]

def left(bitree):
    return bitree[2]

def set_left(bitree, left):
    bitree[1] = left

def set_right(bitree, right):
    bitree[2] = right


# 表达式树

from numbers import Number

def make_sum(a, b):
    return ['+', a, b]

def make_prod(a, b):
    return ['*', a, b]

def make_diff(a, b):
    return ['-', a, b]

def make_div(a, b):
    return ['/', a, b]

def is_basic_exp(a):
    return not isinstance(a, list)

def is_compose_exp(a):
    return isinstance(a, list)

def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]),  eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError("Unknown operator:", op)

def eval_sum(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a + b
    if isinstance(a, Number) and a == 0:
        return b
    if isinstance(b, Number) and b == 0:
        return a
    return make_sum(a, b)

def eval_diff(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a - b
    if isinstance(a, Number) and a == 0:
        return -b
    if isinstance(b, Number) and b == 0:
        return a
    return make_diff(a, b)

def eval_prod(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a * b
    if (isinstance(a, Number) and a == 0 or
        isinstance(b, Number) and b == 0):
        return 0
    if isinstance(a, Number) and a == 1:
        return b
    if isinstance(b, Number) and b == 1:
        return a
    return make_prod(a, b)

def eval_div(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a / b
    if isinstance(a, Number) and a == 0:
        return 0
    if isinstance(b, Number) and b == 0:
        raise ZeroDivisionError
    if isinstance(b, Number) and b == 1:
        return a
    return make_div(a, b)

