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










