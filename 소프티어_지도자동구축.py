# 사각형 개수 공식=> 4 ** (현재 단계 index)
# 점의 개수 => 4 - 9(4+1+4) - 25(4+9+12(2*3*2)) - 25+16+40(5*4*2)
# 점의 개수 공식 => (이전 단계 점의 개수) + (이전 단계 사각형 개수) + ( 이전 단계 변의 개수 )
# 변의 개수 공식 => ((한 변의 점의 개수 -1 ) * 점의 개수)*2
# https://softeer.ai/practice/info.do?idx=1&eid=413&sw_prbl_sbms_sn=181533
import sys
input = sys.stdin.readline

x = int(input())
arr = [4] + [0] * x

if x > 0:
    for n in range(1, x + 1):
        square = 4 ** (n-1)
        lastpoints = arr[n-1]
        plussquarepoing = ((arr[n-1] ** (1/2)) -1 ) * (arr[n-1] ** (1/2)) * 2
        arr[n] = int(square + lastpoints + plussquarepoing)
print(arr[x])
