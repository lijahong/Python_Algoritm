# 오름차순 정렬 필요 -> 따라서, 이전 원소보다 크면 ans 에 넣게 한다.
# 이때, 처음에는 비어있으므로 0 을 넣고, 출력시 인덱스1부터 출력하게 설정
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
ans = [0]

def backtracking():
    if (len(ans)-1) == b:
        print(" ".join(map(str,ans[1:])))
        return
    for i in range(1,a+1):
        if (i not in ans) and i > ans[-1]:
            ans.append(i)
            backtracking()
            ans.pop()
backtracking()
