import sys
n = int(sys.stdin.readline())
board = list()
persentage = list()

for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
    result = sum(board[i][1:len(board[i])])/board[i][0]
    people = 0
    for j in range(1,board[i][0] + 1):
        if board[i][j] > result :
            people += 1
    persentage.append((people/board[i][0] * 100))

for x in range(n):
    answer = "{:.3f}%".format(persentage[x])
    print(answer)
