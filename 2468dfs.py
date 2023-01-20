# 2 차원 배열의 최대 값 구하기 -> map 이용 -> maxvalue = max(map(max,배열)) -> 이러면, 각 행의 최댓값을 가져온 다음, 가져온 최댓값 중에서 최대값을 반환한다.
# 모든 높이에 대해 안전 구역을 구한 뒤, 최대값을 반환 -> 연결된 안전 구역이 하나이므로 dfs 로 푼다.
# dfs 를 돌릴때, 구역의 모든 노드에서 dfs를 돌리도록 2중 반복문을 사용한다. 안전구역의 어떤 노드에서 시작하든 재귀를 통해 인접한 안전 구역 노드를 모두 찾아내고, 방문 여부를 나타내는 visit에 표시하기에, 2중 반복문에서 방문한 구역에 대해 dfs를 다시 실행하면 False를 반환하여 count가 증가하지 않는다.
# 따라서, 안전구역의 한 노드에서 dfs를 돌리면, 인접한 모든 안전구역을 방문하여 하나의 안전 구역임을 알아낸다.
# 단, 모든 높이에 대해 2중 반복문을 반복해야 하므로, 만약 배열board에서 방문한 노드의 값을 변경하면, 다음번 높이에 대한 실행에 영향을 끼친다. 따라서, 각 높이에 대한 탐색 과정마다 방문 여부를 나타내는 visit 배열을 선언하여 사용한다.

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
board = list()
for _ in range(n):
    board.append(list(map(int,input().split())))

xmove = [0,0,-1,1]
ymove = [-1,1,0,0]
answer = 0

def dfs(x,y,up):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if board[x][y] > up and visit[x][y] == False:
        visit[x][y] = True
        for i in range(4):
            dfs(x + xmove[i],y + ymove[i],up)
        return True
    return False

maxvalue = max(map(max,board))

for up in range(0,maxvalue + 1):
    count = 0
    visit = [[False for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i,j,up):
                count += 1
    answer = max(answer,count)
print(answer)
