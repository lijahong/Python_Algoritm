import sys
n = int(sys.stdin.readline())

graph = list()
result = list()
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x >= 0 and y >= 0 and x < n and y < n:
        if graph[x][y] == 1:
            if (x,y) not in visit:
                visit.append((x,y))
                graph[x][y] = 0
                dfs(x-1,y)
                dfs(x,y-1)
                dfs(x+1,y)
                dfs(x,y+1)

for i in range(n):
    for j in range(n):
        visit = list()
        dfs(i,j)
        if len(visit) > 0 :
            result.append(len(visit))

result.sort()
print(len(result))
for p in range(len(result)):
    print(result[p])
