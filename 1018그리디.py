# 모든 경우에 대해 확인한다. 모든 체스판의 경우에서 해당 체스판의 모든 문자를 탐색한다.
# 이때, w 시작 경우와 b 시작 경우중에서도 최소를 골라야하므로, index1 과 index2 를 통해 각 경우에서 최소를 고른다.
# W시작의 경우 짝수일때, B이면 증가, 홀수일때, W 이면 증가이고,
# B시작의 경우 짝수일때, W이면 증가, 홀수일때, B 이면 증가한다.

import sys

input = sys.stdin.readline
answer = 2500
x,y = map(int,input().split())
board = list()
for _ in range(x):
    board.append(list(input().strip("\n")))

for i in range(x-7):
    for j in range(y-7):
        index1 = 0 #b시작 경우
        index2 = 0 #w시작 경우
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] == 'W':
                        index1 += 1
                    else:
                        index2 += 1
                else:
                    if board[a][b] == 'B':
                        index1 += 1
                    else:
                        index2 += 1
        answer = min(answer, min(index1,index2))
print(answer)
