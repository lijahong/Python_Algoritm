# 1 조합 라이브러리 사용
# print 할때 앞에 * 을 붙이면 리스트나 튜플의 요소를 전부 일렬로 출력한다

import sys
input = sys.stdin.readline

from itertools import permutations
n = int(input())
numlist = list()

for i in range(1,n+1):
    numlist.append(i)

for i in permutations(numlist,n):
    print(*i)

# 2 백트래킹 사용
# n까지의 수를 모두 넣는데, 이때 해당 수가 리스트에 없으면 넣고, 재귀함수를 돌린다. 이때 리스트의 길이가 n이라면, 출력 후 넣은 수를 pop 한다.
# 이는, 순서에 영향이 있는 순열이기에 가능

import sys
input = sys.stdin.readline

n = int(input())
numlist = list()
def backtracking(n):
    if len(numlist) == n:
        print(*numlist)
        return
    else:
        for i in range(1,n+1):
            if i not in numlist:
                numlist.append(i)
                backtracking(n)
                numlist.pop()
backtracking(n)
