import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

n,m,r = map(int,input().split())
graph = [[] for _ in range(n)]
visit = [0 for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def bfs(node):
    queue = deque([node])
    count = 0
    while queue:
        cnode = queue.popleft()
        if visit[cnode] == 0:
            count += 1
            visit[cnode] = count
            graph[cnode].sort()
            queue.extend(graph[cnode])
bfs(r-1)
for i in visit:
    print(i)