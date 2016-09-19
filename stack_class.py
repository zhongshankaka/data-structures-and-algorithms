# -*- coding: utf-8 -*-

#连续栈
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

#
# # 链接栈
#
# from single_linked_list import LNode
#
# class StackUnderflow(ValueError):
#     pass
#
#
# class LStack():
#     def __init__(self):
#         self.top = None
#
#     def is_empty(self):
#         return self.top is None
#
#     def top(self):
#         if self.top is None:
#             raise StackUnderflow
#         return self.top.elem
#
#     def push(self, elem):
#         self.top = LNode(elem, self.top)
#
#     def pop(self):
#         if self.top is None:
#             raise StackUnderflow
#         e = self.top.elem
#         self.top = self.top.next
#         return e


# 括号匹配
class ESStack(SStack):
    def depth(self):
        return len(self.elems)

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



if __name__ == "__main__":
    check_pares("{[[)]}")












