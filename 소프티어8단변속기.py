#연속 증가인지 감소인지 판단하는 문제

import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))

if arr[0] < arr[1]:
    answer = 'ascending'
else:
    answer = 'descending'

for i in range(len(arr) - 1):
    if (arr[i] > arr[i+1] and answer == 'ascending') or (arr[i] < arr[i+1] and answer == 'descending'):
        answer = 'mixed'

print(answer)
