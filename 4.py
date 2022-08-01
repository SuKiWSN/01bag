"""
***滚动数组法***

"""
from itertools import combinations
import numpy as np
import os
from init import init

def get_maxvalue(t1, t2):
    for i in range(N):
        for j in range(1, V+1):
            if j < v[i]:
                t2[j] = t1[j]
            else:
                t2[j] = max(t1[j], t1[j-v[i]]+w[i])
        t = t1
        t1 = t2
        t2 = t


if __name__=='__main__':
    N, V, v, w = init()
    dp = [np.zeros(1100), np.zeros(1100)]
    t1 = dp[0]
    t2 = dp[1]
    get_maxvalue(t1, t2)
    print(t1[V])
