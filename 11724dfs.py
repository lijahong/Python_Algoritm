# 연결 요소를 구하는 dfs 문제
# 간선 정보를 통해 인접 리스트를 만들고, dfs를 돌려서 연결 요소의 개수를 찾는다.
# 방문한 노드를 처리하여, 다시 방문 시 False를 반환하게 한다. 이를 통해 중복 방문을 막을 수 있다.

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

a,b = map(int,input().split())
visit = [False for _ in range(a + 1)]
board = [[]for _ in range(a + 1)]

for _ in range(b):
    x,y = map(int,input().split())
    board[x].append(y)
    board[y].append(x)

def dfs(x):
    if visit[x] == False:
        visit[x] = True
        for i in board[x]:
            dfs(i)
        return True
    return False
count = 0
for i in range(1,a+1):
    if dfs(i):
        count += 1
print(count)
