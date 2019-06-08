import numpy as np
import pandas as pd
import decimal as dc
from collections import defaultdict
from itertools import chain


class Cluster():

    def __init__(self, V, h, k, n):
        self.V = V
        self.h = h
        self.k = k
        self.n = n


def initializeClusters(matrix):
    cluster_list = list()
    for i in range(len(matrix)):
        cluster_list.append(Cluster(np.zeros((1, 1)).astype(float), 0, float(1), f"{i}"))
    return cluster_list

def getNearestClusters(matrix):
    n, mi, mj = len(matrix), 0, 1
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] < matrix[mi][mj]:
                mi, mj = i, j
    return mi, mj

def UPGMA(D, n):
    # print(n)
    initial_clusters, adj_list = initializeClusters(D), defaultdict(list)
    while len(initial_clusters) > 1:
        mi, mj = getNearestClusters(D)
        node1, node2 = initial_clusters[mi], initial_clusters[mj]
        n_new = len(node1.V) + len(node2.V) + 1
        new_V, new_h, new_k = np.zeros((n_new, n_new)), float(D[mi][mj] / 2), node1.k + node2.k

        for i in range(0, len(node1.V)):
            for j in range(0, len(node1.V)):
                new_V[i + 1][j + 1] = node1.V[i][j]
        for k in range(0, len(node2.V)):
            for l in range(0, len(node2.V)):
                new_V[k + len(node1.V) + 1][l + len(node1.V) + 1] = node2.V[k][l]
        new_V[1][0] = new_V[0][1] = new_h - node1.h
        new_V[len(node1.V) + 1][0] = new_V[0][len(node1.V) + 1] = new_h - node2.h

        saved, excluded = min(mi, mj), max(mi, mj)
        adj_list[n].append(f"{n}->{node1.n}:{round(dc.Decimal(new_h - node1.h), 3)}")
        adj_list[int(node1.n)].append(f"{node1.n}->{n}:{round(dc.Decimal(new_h - node1.h), 3)}")
        adj_list[n].append(f"{n}->{node2.n}:{round(dc.Decimal(new_h - node2.h), 3)}")
        adj_list[int(node2.n)].append(f"{node2.n}->{n}:{round(dc.Decimal(new_h - node2.h), 3)}")

        for x in range(0, len(D)):
            D[x][saved] = D[saved][x] = float((D[saved][x]*node1.k
                                         + D[excluded][x]*node2.k) / new_k)

        D = np.delete(np.delete(D, excluded, 0), excluded, 1)
        np.fill_diagonal(D, 0)

        initial_clusters[mi] = Cluster(new_V, new_h, new_k, f"{n}")
        del initial_clusters[mj]

        n += 1

    return adj_list
    
    
    
''' A Rosalind-flavoured parser '''
test_array = np.array(pd.read_csv(str(input)), skiprows=[0], sep='\t', header=None)).astype(float)
size = len(test_array)
res = UPGMA(test_array, size)
print('\n'.join(list(chain.from_iterable([res[x] for x in sorted(res.keys())]))))
