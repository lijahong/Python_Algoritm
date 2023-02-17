# 배열 비교 문제

import sys
input = sys.stdin.readline

m,n,k = map(int,input().split())
secretnum = list(map(int,input().split()))
button = list(map(int,input().split()))
answer = 'normal'
for i in range(0,n-m+1):
    if button[i:i+m] == secretnum:
        answer = 'secret'
print(answer)
