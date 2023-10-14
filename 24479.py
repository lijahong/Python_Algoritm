import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(visit, startnode, graph):
    global count
    count += 1
    visit[startnode] = count
    graph[startnode].sort()
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


###################### 다른 풀이 ##########################
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n)]
visit = [ 0 for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

count = 0
def dfs(node):
    global count
    count += 1
    visit[node] = count
    graph[node].sort()
    for i in graph[node]:
        if visit[i] == 0:
            dfs(i)
dfs(r -1)
for i in visit:
    print(i)
