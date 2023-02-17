# 전형적인 dfs 문제
# 마지막에 장애물 수를 오름차순으로 정렬하는 것에 주의하자.
# dfs에 들어온 좌표가 맵 밖이라면 false, 아닐 경우 1이라면 장애물 개수를 증가시키고 해당 노드의 값을 0으로 바꾼다. 이후 4방향에 대해 재귀함수 호출한다.

import sys
input = sys.stdin.readline

def dfs(x, y):
    global count
    if x < 0 or x >= num or y < 0 or y >= num:
        return False

    if arr[x][y] == 1:
        count += 1
        arr[x][y] = 0
        for i in range(4):
            dfs(x + dx[i],y + dy[i])
        return True
    return False

num = int(input())
arr = list()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
countlist = list()
for _ in range(num):
    arr.append(list(map(int,input().strip())))

for i in range(num):
    for j in range(num):
        if arr[i][j] == 1:
            count = 0
            if dfs(i,j) == True:
                answer += 1
                countlist.append(count)

print(answer)
countlist.sort()
for i in countlist:
    print(i)
