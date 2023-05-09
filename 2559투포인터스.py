# 먼저, 투포인터스 ( 연속된 수의 뭐시기 구하기 ) 할 때, while 문은 무한 반복으로 하자. break를 통해 중지되게 하자
# 둘째, 모든 수가 음수인 가능성에서 answer 배열을 0으로 미리 정의했을 때, 배열의 범위를 잘못 설정하면, 초과된 분량의 0 이 가장 커질 수 있으니, 배열을 미리 선언할 때, 범위에 주의하자

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
arr = list(map(int,input().split()))

answer = [0 for _ in range(a-b + 1)]
start = -1
end = -1
sumx = 0

while True:
    if (end - start) < (b):
        end += 1
        if end >= a:
            break
        sumx += arr[end]
    else :
       start += 1 
       answer[start] = sumx
       sumx -= arr[start]
print(max(answer))

# 슬라이딩 윈도우로 푼 방식
# 1. 첫번째 무리의 합을 구하고
# 2. 맨앞을 빼고, 맨뒤의 뒤에걸 더하는 방식

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
arr = list(map(int,input().split()))

sumx = maxx = sum(arr[0:b])
for i in range(0,a-b):
    sumx = sumx + arr[i+b] - arr[i]
    maxx = max(maxx,sumx)
print(maxx)
