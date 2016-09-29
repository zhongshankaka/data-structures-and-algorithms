# -*- coding: utf-8 -*-

from stack_class import *
from queue_class import *

maze1 = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1],
  [1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1],
  [1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
  [1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],
  [1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1],
  [1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1],
  [1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1],
  [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
  [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
  [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
  [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1],
  [1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
  [1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
  [1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0


# 递归路径搜索

def maze_solver_rec(maze, start, end):
    def find_path(maze, start, end):
        mark(maze, start)
        if start == end:
            print(start, end='')
            return True
        for i in range(4):
            nextp = start[0]+dirs[i][0], start[1]+dirs[i][1]
            if passable(maze, nextp):
                if find_path(maze, nextp, end):
                    print(start, end='')
                    return True
        return False

# 回溯法

def print_path(end, last, st):
    print(end, last, sep=' ', end='')
    while not st.is_empty():
        print(st.pop[0], end='')
    print('\n')


def print_path_rev(end, last, st):
    path = [end, last]
    while not st.is_empty():
        path.append(st.pop())
    path.reverse()
    for pos in path:
        print(pos, end='')
    print('\n')


def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if nextp == end:
                print_path(end, pos, st)
                return
            if passable(maze, nextp):
                st.push((pos, i+1))
                mark(maze, nextp)
                st.push((nextp, 0))
                break
    print("No path found.")


# 使用队列

def maze_solver_queue(maze, start, end):
    if start == end:
        print("Path finds.")
        return
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print("Path finds.")
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)
    print("No path.")


# 返回路径

def build_path(start, pos, end, precedent):
    path = [end]
    while pos != start:
        path.append(pos)
        pos = precedent[pos] #得到前一位置
    path.append(start)
    path.reverse()
    return path

def maze_solver_queue1(maze, start, end):
    if start == end:
        return [start]
    qu = SQueue()
    precedent = dict()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    return build_path(start, pos, end, precedent)
                mark(maze, nextp)
                precedent[nextp] = pos #在dict中记录前一位置
                qu.enqueue(nextp)
    print("No path.")


















