# 적록색약일때와 아닐때를 각각 구해야하므로, 방문 여부 배열과 영역값 변수를 두개를 사용한다. 이를 통해 전체 영역에 대한 탐색을 두번이 아닌 한번으로 문제를 해결할 수 있다.
# 적록색약이 아닐 경우, 하나의 영역에 대해 처음 방문한 노드의 값과 같은 노드들이 하나의 영역이므로, 해당 위치의 영역값을 dfs의 매개변수에 준다.
# 파이썬은 문자열을 내부적으로 배열로 처리한다. 따라서 in을 이용하여 현재 위치의 값과 처음 방문한 노드의 값을 비교한다. 
# 배열이 아닌 "B" 문자열 하나만 주더라도, 이를 배열로 처리하므로 in 연산이 가능하다.
# 적록색약일 경우, 해당 위치값이 R이나 G라면, dfs에 넘겨줄 비교 배열값을 ['R','G']로 설정하여 R과 B를 하나의 배열에 넣어 같은 영역으로 구분할 수 있게 한다.

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(str,input().strip("\n"))))

def dfs(x,y,isarr,visit):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] in isarr and visit[x][y] == False:
        visit[x][y] = True
        dfs(x - 1,y,isarr,visit)
        dfs(x + 1, y, isarr,visit)
        dfs(x, y + 1, isarr,visit)
        dfs(x, y - 1, isarr,visit)
        return True
    return False

count1 = 0
count2 = 0
visit1 = [[False for _ in range(n)]for _ in range(n)]
visit2 = [[False for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i,j,arr[i][j],visit1) == True:
            count1 += 1
        if arr[i][j] in ['R','G']:
            isarr = ['R','G']
        else:
            isarr = ['B']
        if dfs(i,j,isarr,visit2) == True:
            count2 += 1

print(count1,count2)
