import sys
from collections import deque
input = sys.stdin.readline
graph = list()
n,m = map(int,input().split())

for _ in range(m):
    graph.append(list(map(int,input().split())))

queue = deque()

for q in range(m):
    for e in range(n):
        if graph[q][e] == 1:
            queue.append((q,e))

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    answer = 0
    while queue:
        a,b = queue.popleft()
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n :
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[a][b] + 1
                    queue.append((nx,ny))
        answer = graph[a][b]
    return ( answer - 1)

answer = bfs()

for ax in range(m):
    for ay in range(n):
        if graph[ax][ay] == 0:
            print(-1)
            exit(0)
print(answer)
