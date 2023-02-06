# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
# 프로그래머스 dfs 네트워크 레벨 3
# 인접 행렬을 인접 리스트 형태로 변환 후 dfs 를 한다. 각 노드당 dfs를 돌려서 인접 노드의 방문을 True로 바꿔준다. 해당 노드에 처음 방문하면 True를 반환하며, 재귀를 통해 인접한 모든
# 노드를 방문 처리한다.

def solution(n, computers):
    answer = 0
    connectlist = [[] for _ in range(n)]
    visit = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                connectlist[i].append(j)
    for i in range(n):
        if dfs(visit,i,connectlist) == True:
            answer += 1
    return answer

def dfs(visit,n,connectlist):
    if visit[n] == False:
        visit[n] = True
        for i in connectlist[n]:
            dfs(visit,i,connectlist)
        return True
