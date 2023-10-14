from collections import deque
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visit = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    def bfs(start):
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if visit[node] == False:
                visit[node] = True
                queue.extend(graph[node])
    for i in range(n):
        if visit[i] == False:
            answer += 1
            bfs(i)    
                
    return answer