from collections import deque
def solution(maps):
    answer = 0
    queue = deque([(0,0)])
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    maxx,maxy = len(maps) - 1, len(maps[0]) - 1
    print(maxx, maxy)
    while queue:
        x,y = queue.popleft()
        if x == maxx and y == maxy:
            answer = maps[x][y]
            break
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            if 0<= dx <= maxx and 0<= dy <= maxy and maps[dx][dy] == 1:
                maps[dx][dy] = maps[x][y] + 1
                queue.append((dx,dy))
    if maps[maxx][maxy] == 1:
        answer = -1
    return answer