# -*- coding: utf-8 -*-

# 邻接矩阵

infinity = float("inf")

class AdjGraphError(TypeError):
    pass


class Graph:
    def __init__(self, mat, unconn=0):
        vnum1 = len(mat)
        for x in mat:
            if len(x) != vnum1:
                raise ValueError("Argument for 'GraphA' is bad.")
        self.mat = [mat[i][:] for i in range(vnum1)]
        self.unconn = unconn
        self.vnum = vnum1

    def vertex_num(self):
        return self.vnum

    def add_edge(self, vi, vj, val=1):
        assert 0 <= vi <self.vnum and 0 <= vj <self.vnum
        self.mat[vi][vj] = val

    def add_vertex(self):
        raise AdjGraphError

    def get_edge(self, vi, vj):
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum
        return self.mat[vi][vj]

    def out_edges(self, vi):
        assert 0 <= vi < self.vnum
        return self._out_edges(self.mat, vi, self.unconn)

    @staticmethod
    def _out_edges(mat, vi, unconn):
        edges = []
        row = mat[vi]
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return "[\n" + "\n".join(map(str, self.mat)) + "\n]"\
                + "\nUnconnected:" + str(infinity)
#
# if __name__ == '__main__':
#
#     g2 = Graph(10, infinity)
#     print(str(g2))
#
#
# # 邻接表
#
class GraphA(Graph):
    def __init__(self, mat, unconn=0):
        vnum1 = len(mat)
        for x in mat:
            if len(x) != vnum1:
                raise ValueError("Argument for 'GraphA' is bad.")
        self.mat = [Graph._out_edges(mat, i, unconn)
                        for i in range(vnum1)]
        self.vnum = vnum1
        self.unconn = unconn

    def add_vertex(self):
        self.mat.append([])
        self.vnum += 1
        return self.vnum

    def add_edge(self, vi, vj, val=1):
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum
        row = self.mat[vi]
        for i in range(len(row)):
            if row[i][0] == vj:
                self.mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
                break
        else:
            i += 1
        self.mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum
        for i, val in self.mat[vi]:
            if i == vj:
                return val
        return self.unconn

    def out_edges(self, vi):
        assert 0 <= vi < self.vnum
        return self.mat[vi]


from stack_class import SStack, StackUnderflow

# 深度优先遍历

def DFS_seq(graph, v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop() # edges为某顶点边表，i为边表下标
        if i < len(edges):
            v, e = edges[i]
            st.push((i+1, edges))
            if not visited:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq

# DFS生成树

def DFS_span_tree(graph):
    vnum = graph.vertex_num()
    span_forest = [None]*(vnum)
    def dfs(graph, v):
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)

    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return span_forest


if __name__ == '__main__':
    gmat1 = [[0, 1, 1, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0]]

    gmat2 = [[0, 1, 0, 1, 1, 1, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 1, 0]]

    g1 = GraphA(gmat1, 0)
    dfs1 = DFS_seq(g1, 0)
    print(dfs1)

    g2 = GraphA(gmat2, 0)
    dfs2 = DFS_seq(g2, 0)
    print(dfs2, "\n")

    dfs_tree = DFS_span_tree(g1)
    print(dfs_tree)
    dfs_tree = DFS_span_tree(g2)
    print(dfs_tree)
