"""
***回溯法***

"""
from itertools import combinations
import numpy as np
import os
from init import init

def backtrack(i, N):
    global bestW, curV, curW
    if i >= N:
        if bestW < curW:
            bestW = curW
        return
    else:
        if curV + v[i] <= V:
            x[i] = True
            curW += w[i]
            curV += v[i]
            backtrack(i+1, N)
            curW -= w[i]
            curV -= v[i]

        x[i] = False
        backtrack(i+1, N)



if __name__=='__main__':
    bestW = 0
    curW = 0
    curV = 0
    N, V, v, w = init()
    x = [False for i in range(N)]
    backtrack(0, N)
    print(bestW)