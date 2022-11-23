import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(visit, startnode, graph):
    global count
    count += 1
    visit[startnode] = count
    graph[startnode].sort(reverse=True)
    for node in graph[startnode]:
        if visit[node] == 0:
            dfs(visit, node, graph)


n,m,r = map(int,input().split())

a = [0 for _ in range(n+1)]
b = [[] for _ in range(n+1)] # 간선의 수가 아니라 각 노드당 접근한 놈임

for _ in range(m):
    x,y = map(int,input().split())
    b[x].append(y)
    b[y].append(x)

count = 0

dfs(a,r,b)
for i in range(1, n + 1):
    print(a[i])
