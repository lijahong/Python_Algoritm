# 아리스토텔레스의 체 사용 -> 2부터 시작하여 해당 수가 소수라면, 소수 리스트에 추가한다. 이때, 해당 수의 배수는 소수가 아니므로 반복문을 통해 해당 수의 배수는 모두 소수가 아니라고 지정한다.
# 투포인터스 알고리즘을 이용해 -1 부터 시작하여 수보다 작으면, right 를 증가하여 더하고, 크거나 같으면 left 를 증가하여 뺀다.
# left 에 위치한 수는 빼므로, 사실상 left + 1 ~ right 의 수를 더한 것이다. 따라서 단일 수를 더할 경우 left = right - 1 이다. left와 right 가 같으면, 두 포인터는 같은 위치이므로 합이 0 이 된다.
# right 가 범위를 벗어나면, 반복문을 종료한다.

import sys
input = sys.stdin.readline

a = int(input())
sosulist = list()
sosuright = [False,False] + [True] *(a-1)

for i in range(2,a+1):
    if sosuright[i]:
        sosulist.append(i)
        for j in range(2*i,a+1,i):
            sosuright[j] = False

left,right = -1,-1
answer = 0
sum = 0

while True:
    if sum < a:
        right += 1
        if right >= len(sosulist):
            break
        sum += sosulist[right]
    elif sum >= a:
        if sum == a:
            answer += 1
            left += 1
            sum -= sosulist[left]
        else:
            left += 1
            sum -= sosulist[left]

print(answer)
