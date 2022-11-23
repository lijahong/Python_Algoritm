import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,startnode,visit):
    queue = deque([startnode])
    while queue:
        node=queue.popleft()
        if visit[node] == 0:
            visit[node] = 1
            queue.extend(graph[node])

n = int(input())
com = [ [] for _ in range(n+1)]
visit = [ 0 for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)

bfs(com,1,visit)
print(sum(visit)- 1)
