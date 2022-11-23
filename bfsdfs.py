from collections import deque

def dfs(graph, startnode):
    visit = list()
    stack = list()
    stack.append(startnode)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))
    return visit

def bfs(graph,startnode):
    visit = list()
    queue = deque([startnode])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

def dfs2(graph, startnode, visit):
    visit[startnode] = True
    print(startnode, end=' ')

    for node in graph[startnode]:
        if not visit[node]:
            dfs2(graph,node,visit)


visit = [False for _ in range(9)]

graph = [ [],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] # index 는 정점을 나타내는데, 정점은 1 부터 시작하고, index 는 0 부터 시작하므로 앞에 [] 를 하나 추가한다

startnode = 1

print(dfs(graph,startnode))
print(bfs(graph,startnode))
print(dfs2(graph,startnode,visit))
