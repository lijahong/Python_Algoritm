# 미로탈출과 같은 bfs 문제
# deque 선언 시, 안에 원소를 넣을려면, 무조건 [] 안에 넣어야한다.
# popleft 시, 나온게 배열이나 튜플이면, 해당 배열이나 튜플에 들어있는 값을 각각 다른 변수에 지정할 수 있다. ex) x,y = queue.popleft() 하면 안에 있는게 [1,2] 나 (1,2) 일 경우, x와y에 각각 1과 2가 들어간다.
# 맵 크기가 따로 변수로 주어지지 않으므로, 세로 길이는 len(maps)로, 가로 길이는 len(maps[0])로 지정한다.
# 미로탈출 형식의 bfs는 갈 수 있는 칸에 위치했던 순서를 기록하므로, 목적지에 저장된 값이 가장 빨리 목적지에 도달했을때, 이동한 순서이다.

from collections import deque
def solution(maps):
    answer = 0
    bfs(maps)
    answer = maps[len(maps)-1][len(maps[0])-1]
    if answer == 1:
        answer = -1
    return answer

def bfs(maps):
    queue = deque([(0,0)])
    xmove = [0,0,-1,1]
    ymove = [-1,1,0,0]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            x1 = xmove[i] + x
            y1 = ymove[i] + y
            if 0<= x1 < len(maps) and 0 <= y1 < len(maps[0]):
                if maps[x1][y1] == 1:
                    maps[x1][y1] = maps[x][y] + 1
                    queue.append((x1,y1))
