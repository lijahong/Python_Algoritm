# 빠르게 100번 까지 갈 수 있는 횟수
# 1부터 6까지 더할 수 있으므로, 해당 칸에 방문 하지 않았다면, 해당 칸에 이전 칸 + 1 을 저장하고, 방문할 노드를 의미하는 큐에 삽입
# 이때, 더한게 100을 넘어가면, 인덱스가 초과할 수 있으니 continue
# 사다리와 뱀의 경우, 방문노드가 해당하면, 방문 노드 인덱스 값을 바꾸고, 이동한 칸의 값 ( 이동 횟수 )에 이전 노드의 값을 넣는다

import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
ladder=list()
snake=list()
for _ in range(a):
    n,m = map(int,input().split())
    ladder.append([n,m])
for _ in range(b):
    n,m = map(int,input().split())
    snake.append([n,m])

board = [0 for _ in range(101)]

def bfs():
    queue = deque([1])
    while queue:
        a = queue.popleft()
        if a == 100:
            print(board[100])
            break
        for i in ladder:
            if a == i[0]:
                board[i[1]] = board[a]
                a = i[1]
        for i in snake:
            if a == i[0]:
                board[i[1]] = board[a]
                a = i[1]
        for i in range(1,7):
            if (a + i) > 100:
                continue
            if board[a + i] == 0:
                queue.append(a+i)
                board[a+i] = board[a] + 1
bfs()
