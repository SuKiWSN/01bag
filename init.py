"""
***初始化***

N: 物品数量
V: 背包容量
v: 每个物品体积
w: 每个物品价值

"""

import numpy as np

def init():
    V, N = [int(i) for i in input().split(' ')]
    v = []
    w = []
    for _ in range(N):
        vi, wi = input().split(' ')
        v.append(int(vi))
        w.append(int(wi))

    v = np.array(v)
    w = np.array(w)
    return N, V, v, w