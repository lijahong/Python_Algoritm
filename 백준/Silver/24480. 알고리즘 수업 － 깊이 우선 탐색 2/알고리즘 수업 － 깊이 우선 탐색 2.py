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
    graph[node].sort(reverse=True)
    for i in graph[node]:
        if visit[i] == 0:
            dfs(i)
dfs(r -1)
for i in visit:
    print(i)