# 두 포인터가 같은 방향으로 가는 투포인터스 문제
# 두 포인터 사이 값이 목표값보다 작으면, 오른쪽 포인터를 움직이고, 값을 더한다.
# 두 포인터 사이 값이 목표값보다 크면, 최소 길이를 찾기 위해 왼쪽 포인터를 움직이고, 해당 포인터의 값을 뺀다
# 두 포인터는 -1 부터 시작한다. -1 부터 시작하므로 실질적인 수열 범위는 a 포인터 ~ b 포인터가 아닌, a 포인터 + 1 ~ b 포인터 이다. 따라서 길이를 구할 때, 1을 더하지 않는다.
# 두 포인터가 0 부터 시작할려면, 합의 시작이 0이라면 해당 수 증감 후 포인터 증감을 하고, 배열의 첫번째 수부터 시작한다면, 포인터 증감후 해당 수를 증감한다. 
# 그렇게 값이 작아지다가 다시 목표값보다 작아지면, 다시 오른쪽 포인터를 움직이고, 값을 더한다.
# 그러다가 오른쪽 포인터가 리스트를 벗어나면, 반복문을 중단시킨다. 중단되었을때, 답의 값이 전체 리스트 길이 보다 크다면, 해당 리스트의 부분 수열의 합이 목표값 이상이 되지 못한 것 이므로, 0을 출력한다.

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
arr = list(map(int,input().split()))

answer = a + 1
start,end = -1,-1
sums = 0
while True:
    if sums < b:
        end += 1
        if end >= a:
            break
        sums += arr[end]
    elif sums >= b:
        answer = min(answer,end-start)
        start += 1
        sums -= arr[start]

if answer == (a+1):
    print("0")
else:
    print(answer)
