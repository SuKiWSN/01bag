"""

***暴力求解***

"""
from itertools import combinations
import numpy as np
import os
from init import init

# 计算组合数
def get_combinations(N):
    combination = []
    t = list(range(N))
    for i in range(1, N+1):
        t1 = combinations(t, i)
        for j in t1:
            combination.append(j)
    return combination

def get_maxvalue(combination, v, w):
    maxvalue = 0
    combination = np.array(combination, dtype=object)
    # 计算每个情况的值。比较后得到最大值
    for i in combination:
        sumV = np.sum(v[list(i)])
        if sumV <= V:
            value = np.sum(w[list(i)])
            if value > maxvalue:
                maxvalue = value
    return maxvalue

if __name__=='__main__':
    N, V, v, w = init()
    combination = get_combinations(N)
    # print(combination)
    max_value = get_maxvalue(combination, v, w)
    # os.system('clear')
    print(max_value)