from collections import deque
import sys
input = sys.stdin.readline
start,target = map(int,input().split())
graph = [0 for _ in range(100001)]

queue = deque([start])
graph[start] = 1
while queue:
    node = queue.popleft()
    if node == target:
        print(graph[target] - 1)
        break
    else:
        for i in [node-1, node+1, node*2]:
            if 0<= i < 100001 and graph[i] == 0:
                graph[i] = graph[node] + 1
                queue.append(i)