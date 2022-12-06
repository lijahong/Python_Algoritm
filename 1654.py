import sys
input = sys.stdin.readline

n,m = map(int,input().split())
if n > m:
    exit(0)
lensun = list()
for _ in range(n):
    lensun.append(int(input()))

start = 0
end = max(lensun)
result = 0
while (start <= end):
    mid = ( start + end ) // 2
    if mid < 1:
        break;
    total = 0
    for i in lensun:
            total += (i // mid)
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)
