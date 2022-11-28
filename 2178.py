from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(x,y)])
    graph[x][y] = 1
    while queue:
        a,b = queue.popleft()
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m :
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[a][b] + 1
                    queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
