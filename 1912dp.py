# 연속합의 최댓값 구하기
# answerarr은 이전까지의 합 + 자신과 자신을 비교하여, 최대를 넣는다.
# 연산 종료 후, 연속합 배열에서 최댓값 출력

import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int,input().split()))
answerarr = [arr[0]]

for i in range(len(arr)-1):
    answerarr.append(max(answerarr[i]+arr[i+1],arr[i+1]))
    
print(max(answerarr))

# for 문 범위만 따로 설정한 풀이

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

answerarr = [arr[0]] + [0] * (n-1)
for i in range(1,n):
    answerarr[i] = max(answerarr[i-1] + arr[i] , arr[i])
print(max(answerarr))
