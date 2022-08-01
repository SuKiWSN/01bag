"""
***动态规划***

"""
from itertools import combinations
import numpy as np
import os
from init import init

def get_maxvalue(N, V):
    for i in range(N):
        for j in range(V+1):
            if j < v[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]] + w[i])


if __name__=='__main__':
    N, V, v, w = init()
    dp = np.zeros(N*(V+1)).reshape(N, V+1)
    get_maxvalue(N, V)
    os.system('clear')
    print(dp[N-1][V])
    