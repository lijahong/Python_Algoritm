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

# 불필요한 부분 없앤 코드

import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
miro = list()
for _ in range(a):
    miro.append(list(map(int,input().strip('\n'))))

def bfs():
    queue = deque([(0,0)])
    xm = [-1,1,0,0]
    ym = [0,0,-1,1]
    while queue:
            x,y = queue.popleft()
            for i in range(len(xm)):
                x1 = x + xm[i]
                y1 = y + ym[i]
                if 0<= x1 < a and 0<= y1 < b:
                    if miro[x1][y1] == 1:
                        miro[x1][y1] = miro[x][y] + 1
                        queue.append([x1,y1])
bfs()
print(miro[a-1][b-1])
