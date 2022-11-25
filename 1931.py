import sys
input = sys.stdin.readline

n = int(input())
list = [[] for _ in range(n)]
for i in range(n):
    a,b = map(int,input().split())
    list[i] = [a,b]

list = sorted(list,key = lambda a:a[0]) # 끝나는 시간이 동일한 경우에 대비해 일단 시작 시간 기준 정렬
list = sorted(list,key = lambda a:a[1]) # 끝나는 시간 기준 정렬

count = 0
last = 0
for node in list:
    if node[0] >= last:
        last = node[1]
        count += 1
print(count)
