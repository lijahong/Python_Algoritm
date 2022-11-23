import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
from collections import deque

def bfs(visit, startnode,graph):
    global count
    queue = deque([startnode])
    while queue:
        node = queue.popleft()
        if visit[node] == 0:
            count += 1
            visit[node] = count
            graph[node].sort()
            queue.extend(graph[node])



n,m,r = map(int,input().split())

a = [0 for _ in range(n+1)]
b = [[] for _ in range(n+1)] # 간선의 수가 아니라 각 노드당 접근한 놈임

for _ in range(m):
    x,y = map(int,input().split())
    b[x].append(y)
    b[y].append(x)

count = 0

bfs(a,r,b)
for i in range(1, n + 1):
    print(a[i])
