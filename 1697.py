# n 이 m 에 도달하는데 가장 빠른 시간이므로, queue 에서 m 이 처음 나올 때가 가장 빠른 시간이다. while 이 돌수록 시간이 흐르기 때문이다.
# 범위는 문제에서 주어진데로 설정하자
# 현재 위치에서 인접한 경우에 대해 모두 탐색하기에 bfs

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [0 for _ in range(100001)]
queue = deque([n])
while queue:
    i = queue.popleft()
    if i == m:
        print(graph[i])
        break
    else:
        for j in [i-1,i+1,i*2]:
            if 0 <= j <= 100000 and graph[j] == 0:
                queue.append(j)
                graph[j] = graph[i] + 1
