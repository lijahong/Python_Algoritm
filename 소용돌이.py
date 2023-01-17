# cnt 는 꾸준히 증가. 마지막 수가 n 의 제곱이므로, 이를 초과하면 반복문 종료
# trans 는 방향을 의미한다. 첫 반복문 두번이 끝나면, row 가 감소해야 하므로 -1 을 곱한다
# 반복 횟수는 4 -> 3 -> 2 -> 1 처럼 1씩 감소하므로 반복문이 끝나면 반복 횟수를 1 감소시킨다
# 처음에 trans 를 더해야 하므로 cul ( 열 ) 은 -1부터 시작한다

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0 for _ in range(n)]for _ in range(n)]

row = 0
cul = -1
cnt = 1
trans = 1
maxn = n ** 2
while cnt <= maxn:
    for i in range(n):
        cul += trans
        arr[row][cul] = cnt
        cnt += 1
    n -= 1
    for i in range(n):
        row += trans
        arr[row][cul] = cnt
        cnt += 1
    trans *= -1
print(arr)
