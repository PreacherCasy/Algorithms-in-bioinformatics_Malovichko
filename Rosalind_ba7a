from collections import defaultdict
import numpy as np
from itertools import chain


def dfs_paths(graph, start, goal, leaves)->list:
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        iterator = list(set(map(lambda x: x[0], graph[vertex])) - set(path))
        iterator.sort()
        if iterator:
            for next in iterator:
                if next == goal:
                  path += [next]
                   return path
                else:
                    if next not in leaves:
                      stack.append((next, path + [next]))


def restore_distance_matrix(n: int, adj_list: list) -> np.array:

    mat, adj_dict = np.zeros((n, n)), defaultdict(set)
    leaves = list(map(lambda x: x.split('->')[0], adj_list[:n]))
    for i in adj_list:
        labels, value = i.split(':')
        start, finish = labels.split('->')
        adj_dict[start].add((finish, value))
    for i in range(n):
        for j in range(n):
            if i != j:
                path = dfs_paths(adj_dict, str(i), str(j), leaves=leaves)
                dist =sum(map(int, list(chain.from_iterable(list(map(lambda x: [y[1] for y in adj_dict[path[x]]
                                          if y[0] == path[x+1]], range(len(path) - 1)))))))
                mat[i][j] = mat[j][i] = dist
    return mat.astype(int)

with open(str(input), 'r') as handle:
    lines = list(handle.readlines())
    n, lines = int(lines[0]), list(map(lambda x: x.rstrip('\n'), lines[1:]))

res = restore_distance_matrix(n, lines)

np.savetxt(fname=input(), fmt="%d", comments='',
           X=res, delimiter=' ', newline='\n')
