import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(arr,x,y):
    xi = [0,0,-1,1]
    yi = [-1,1,0,0]
    if x < 0 or x >= b or y < 0 or y >= a:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        for i in range(4):
            dfs(arr,x + xi[i],y + yi[i])
        return True
    return False


n = int(input())
for _ in range(n):
    a,b,c = map(int,input().split())
    arr = [[0 for _ in range(a)]for _ in range(b)]
    for _ in range(c):
        x,y = map(int,input().split())
        arr[y][x] = 1

    count = 0
    for i in range(b):
        for j in range(a):
            if dfs(arr, i, j) == True:
                count += 1
    print(count)
