# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
# 프로그래머스 dfs 네트워크 레벨 3
# 인접 행렬을 인접 리스트 형태로 변환 후 dfs 를 한다. 
# 각 노드당 dfs를 돌려서 인접 노드의 방문을 True로 바꿔준다. 해당 노드에 처음 방문하면 True를 반환하며, 재귀를 통해 인접한 모든 노드를 방문 처리한다. 
# dfs가 True를 반환하면, 연결 값이 증가된다.

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

# 위의 경우 선 dfs 후 연결 노드를 방문 처리해서 반환 값을 통해 방문 여부를 확인하여 연결 값을 증가시켰으면, 밑의 경우 선 방문 여부를 확인하여 연결 값을 증가시키고 후 dfs를 통해 연결 노드를 방문 처리 한다.
# bfs에서는 연결 노드를 모두 방문 처리하여 메인 함수 조건문에서 방문 여부를 확인하여 연결 값을 증가시키는 방식을 했고, dfs에서는 연결 노드를 모두 방문 처리하고, 반환 값을 통해 연결 값을 증가하는 방식을 사용했다.
# 두가지 방식을 반대로 써도 상관 없다. 아래와 같이 dfs에서 메인 함수에서 방문 여부를 확인하여 값을 증가시키고, dfs를 통해 반환 없이 단순 연결 노드 방문 처리만 해도 된다.
    
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
            dfs(visit,i,connectlist)
    return answer

def dfs(visit,n,connectlist):
    if visit[n] == False:
        visit[n] = True
        for i in connectlist[n]:
            dfs(visit,i,connectlist)
