# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
# 프로그래머스 네트워크 bfs 레벨 3
# dfs 방식이랑 비슷하다. 먼저, 인접 행렬을 인접 리스트로 변환하고, 모든 노드에 대한 반복문을 돌리는데, 해당 노드의 방문 여부가 False라면, answer를 증가시키고, bfs를 돌린다.
# bfs를 돌리면, 연결된 노드의 방문 여부가 모두 True로 바뀌기에, 반복문에서 해당 노드에 대한 처리를 할 때, 방문한 노드이기에 answer가 증가하지 않는다.

from collections import deque
def solution(n, computers):
    answer = 0
    connectlist = [[] for _ in range(n)]
    visit = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                connectlist[i].append(j)
    
    for i in range(n):
        if visit[i] == False:
            answer += 1
            bfs(i,visit,connectlist)
    
    return answer

def bfs(n, visit, connectlist):
    queue = deque([n])
    while queue:
        node = queue.popleft()
        if visit[node] == False:
            visit[node] = True
            queue.extend(connectlist[node])
