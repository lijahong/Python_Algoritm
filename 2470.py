# 투 포인터 문제 -> 정렬 후, 최소 보다 작으면 답에 입력한다. 그 후 0 보다 크면, 값을 낮춰야하므로 오른쪽에서 앞으로, 0 보다 작으면 값을 높여야 하므로 왼쪽에서 뒤로 가게 한다
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split(' ')))

start = 0
end = n - 1
minarr = 2e+9+1
arr.sort()
answer = []
while start < end:
    tmp = arr[start] + arr[end]
    if abs(tmp) < minarr:
        minarr = abs(tmp)
        answer= [ arr[start],arr[end]]
    if tmp > 0:
        end -= 1
    elif tmp < 0:
        start += 1
    elif tmp == 0: # 0인 경우를 처리안해줘서 시간초과가 나왔다. 
        answer= [ arr[start],arr[end]]
        break;
print(answer[0],answer[1])
