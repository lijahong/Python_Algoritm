from collections import deque
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[] for _ in range (n+1)]
visit = list()
visit2 = list()

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,v,visit):
    queue = deque([v])
    while queue:
        a = queue.popleft()
        if a not in visit:
            graph[a].sort() # 입력 받은 상태이기에 정렬이 안되있다. 따라서 정렬 해줘야 한다
            visit.append(a)
            queue.extend(graph[a])

def dfs(graph,v,visit):
    visit2.append(v)
    graph[v].sort()
    for node in graph[v]:
        if node not in visit2:
            dfs(graph,node,visit)

bfs(graph,v,visit)
dfs(graph,v,visit2)

print(*visit2) # 리스트에 있는거 전부 한줄로 출력
print(*visit)
