import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def play():
    n,m,r = map(int,input().split())

    a = [0 for _ in range(n+1)]
    b = [[] for _ in range(n+1)]

    for _ in range(m):
        x,y = map(int,input().split())
        b[x].append(y)
        b[y].append(x)

    count = 1

    def dfs(startnode):
        nonlocal count
        a[startnode] = count
        b[startnode].sort()
        for node in b[startnode]:
            if a[node] == 0:
                count += 1
                dfs(node)

    dfs(r)
    for i in range(1, n + 1):
        print(a[i])
play()