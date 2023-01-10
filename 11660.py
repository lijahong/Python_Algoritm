# 백준 구간합 구하기 5 - dp 문제

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i - 1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]


for i in range(m):
    answer = 0
    x1,y1,x2,y2 = map(int,input().split())
    answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1 -1][y1 -1]
    print(answer)