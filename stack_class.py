# -*- coding: utf-8 -*-

# 连续栈

class StackUnderflow(ValueError):
    pass


class SStack():
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems[len(self.elems)-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems.pop()


# 链接栈

from single_linked_list import LNode

class StackUnderflow(ValueError):
    pass


class LStack():
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def top(self):
        if self.top is None:
            raise StackUnderflow
        return self.top.elem

    def push(self, elem):
        self.top = LNode(elem, self.top)

    def pop(self):
        if self.top is None:
            raise StackUnderflow
        e = self.top.elem
        self.top = self.top.next
        return e


# 括号匹配

def check_pares(text):
    pares = "()[]{}"
    open_pares = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}

    def paretheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in pares:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in paretheses(text):
        if pr in open_pares:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print('Unmatching is found at', i, 'for', pr)
            return False
    print("all matched.")
    return True



# if __name__ == "__main__":
    #check_pares("{[[)]}")


# 后缀表达式计算

class ESStack(SStack):
    def depth(self):
        return len(self.elems)


def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

def suf_exp_evaluator(exp):
    operators = '+-*/'
    st = ESStack()
    for x in exp:
        if not x in operators:
            st.push(float(x))
            continue
        if st.depth() < 2:
            raise SyntaxError("Short of operend(s).")
        a = st.pop()
        b = st.pop()

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a

        st.push(c)

    if st.depth() == 1:
        return st.pop()
    else:
        raise SyntaxError("Extra operand(s).")

# 定义一个交互式驱动函数
def suffix_exp_calculator():
    while True:
        try:
            line = input("后缀表达式:")
            if line == 'end':
                return
            res = suffix_exp_evaluator(str(line))
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)

suffix_exp_calculator()


# 中缀表达式转后缀表达式

priority = {"(": 1, "+": 3, "-": 3, "*": 5, "/": 5}
infix_operators = "+-*/"

# 生成器
def token(line):
   i, l = 0, len(line)
   while i < l:
       while line[i].isspace():
           i += 1
       if i >= l:
           break
       if line[i] in infix_operators:
           yield line[i]
           i += 1
           continue
       j = i + 1
       while (j < l and not line[j].isspace() and
              line[j] not in infix_operators):
           if ((line[j] == "e" or line[j] == "E") and
               j+1 < l and line[j+1] == "-"):
               j += 1
           j += 1
       yield line[i:j]
       i = j

def trans_infix_suffix(line):
    st = SStack()
    l = len(line)
    exp = []
    for i in token(line):
        if i not in infix_operators:
            exp.append(i)
        elif st.is_empty() or i == "(":
            st.push(i)
        elif i == ")":
            while not st.is_empty() and st.pop() != "(":
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError("Missing '('.")
            st.pop()
        else:
            while (not st.is_empty() and
                       priority[st.top()] >= priority[i]):
                exp.append(st.pop())
            st.push(i)
    while not st.is_empty():
        if st.top() == "(":
            raise SyntaxError("Extra '(' in expression.")
        exp.append(st.pop())
    return exp






