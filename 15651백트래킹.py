# 수의 중복은 허용, 수열의 중복은 허용 x
# ans 에 들어있는지 확인하는 조건을 없애면 된다

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
ans = []


def back(depth,n,m):
    if depth == m:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,n+1):
        ans.append(i)
        back(depth+1,n,m)
        ans.pop()
back(0,a,b)
