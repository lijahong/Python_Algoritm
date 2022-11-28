n,m = map(int,input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(graph,x,y):
    if x >= n or x < 0 or y < 0 or y >= m :
        return False
    if graph[x][y] == 0 :
        graph[x][y] = 1
        dfs(graph,x-1,y)
        dfs(graph,x,y-1)
        dfs(graph,x+1,y)
        dfs(graph,x,y+1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if( dfs(graph,i,j) == True):
            count +=1
print(count)
