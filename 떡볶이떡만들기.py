import sys
input = sys.stdin.readline

n,m = map(int,input().split())

x = list(map(int,input().split()))

start = 0
end = max(x)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in x:
        if i > mid:
            total += (i - mid)
    if total < m :
        end = mid -1
    elif total >= m :
        result = mid
        start = mid + 1
print(result)
