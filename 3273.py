# 백준 투 포인터
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
count = 0
arr.sort()
x1 = 0
x2 = n-1

while x1 < x2 :
    sumpos = arr[x1] + arr[x2]
    if sumpos == x:
        count += 1
        x1 += 1
        x2 -= 1
    elif sumpos > x:
        x2 -= 1
    else:
        x1 += 1

print(count)
