import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
canvisit = [[0]*n for _ in range(n)]
def bfs(i):
    visit = [False] * n
    queue = deque([i])
    while queue:
        node = queue.popleft()
        for j in range(n):
            if visit[j] == False and graph[node][j] == 1:
                queue.append(j)
                canvisit[i][j] = 1
                visit[j] = True
for i in range(n):
    bfs(i)
for i in canvisit:
    print(*i)