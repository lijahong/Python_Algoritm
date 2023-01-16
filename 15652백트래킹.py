# 수의 중복 허용, 비내림차순
# 중복 허용이니, ans 에 있는지 확인 x, 중복 허용이니 <= 로 비교

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
ans = [0]


def back(depth,n,m):
    if depth == m:
        print(" ".join(map(str,ans[1:])))
        return
    for i in range(1,n+1):
        if ans[-1] <= i:
            ans.append(i)
            back(depth+1,n,m)
            ans.pop()
back(0,a,b)
