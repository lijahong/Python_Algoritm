import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

canvisit = [[0]*n for _ in range(n)]
nearvisit = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            nearvisit[i].append(j)
def bfs(i):
    visit = [False] * n
    queue = deque([i])
    while queue:
        node = queue.popleft()
        for j in nearvisit[node]:
            if visit[j] == False:
                queue.append(j)
                visit[j] = True
                canvisit[i][j] = 1
for i in range(n):
    bfs(i)
for i in canvisit:
    print(*i)