# 1. 조햡 라이브러리 사용 -> 단순히 모든 조합 경우의 수에서 합이 목표가 되는 경우만 찾으면 된다.
import sys
input = sys.stdin.readline
from itertools import combinations
a,b = map(int,input().split())
numlist = list(map(int,input().split()))
answer = 0
for i in range(1,a+1):
    combilist = combinations(numlist,i)
    for j in combilist:
        if sum(j) == b:
            answer += 1
print(answer)

# 2. 백트래킹 사용
# 전역변수를 외부에서 선언했다면, 함수 내부에서 global을 통해 사용을 명시해야 한다.
# return 과 else: 를 하면 안되는 이유 => 현재 리스트의 합이 목표 값이더라도, 추후에 더해지는 값으로 인해 또 목표 값이 될 수 있기 때문이다.
# 따라서 return을 하면 추가 값으로 인해 목표 값을 달성하는 경우를 못 찾고 넘어간다.
# else: 를 하면, 목표 값 이후에 값을 추가하는 것을 진행하지 못한다.
# 부분 수열이므로 중복을 허용하지 않으며, 순서에 상관이 없다. 따라서 인자로 인덱스를 준다. 해당 인덱스에서 재귀 호출 시,
# 현재 인덱스 + 1 한 값을 주어, 합 리스트에 들어가는 값의 중복과 순서에 따른 경우의 수 중복을 막을 수 있다.

import sys
input = sys.stdin.readline
a,b = map(int,input().split())
numlist = list(map(int,input().split()))
answer = 0
sumlist = list()

def backtracking(start):
    global answer
    if sum(sumlist) == b and len(sumlist) > 0:
        answer += 1
    for j in range(start,a):
        sumlist.append(numlist[j])
        backtracking(j + 1)
        sumlist.pop()
backtracking(0)
print(answer)
