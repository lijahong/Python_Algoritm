# 재귀함수 문제
# 전역 함수를 잘 쓰는 문제다
# 문자열 변환에 주의하자

import sys
import math
input = sys.stdin.readline

def funca(tmplist,min_a):
    global min_val, max_val
    length = len(tmplist)
    if length == 1:
        min_val = min(min_val , min_a)
        max_val = max(max_val, min_a)
    elif length == 2:
        tmp = str(int(tmplist[0]) + int(tmplist[1]))
        funca(tmp, min_a + funcb(tmp))
    else:
        for i in range(0,length-2):
            for j in range(i+1,length-1):
                tmp = str(int(''.join(tmplist[0:i+1])) + int(''.join(tmplist[i+1:j+1])) + int(''.join(tmplist[j+1:])))
                funca(tmp, min_a + funcb(tmp))

def funcb(tmplist): # 홀수 개수 측정
    count = 0
    for i in tmplist:
        if (int(i) % 2) != 0:
            count += 1
    return count

n = str(input().strip())
max_val = 0
min_val = math.inf
funca(n,funcb(n))
print(min_val,max_val)
