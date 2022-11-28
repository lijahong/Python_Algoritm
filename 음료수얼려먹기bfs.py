from collections import deque
n,m = map(int,input().split())
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
            if nx < n and nx >= 0 and ny < m and ny >= 0 :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = 1
                    queue.append((nx,ny))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i,j)
            count += 1

print(count)
