# 괄호를 이용해 최소 값을 구하는 문제
# 만약 -가 있다면, 뒤에 + 를 모두 - 로 바꾸면 된다
# sys 라이브러리를 통해 문자열을 입력받으면, 마지막에 줄바꿈 특수 문자가 들어가므로 strip 을 통해 없앤다
# isnumeric 은 빈칸에는 False 를 반환하지 않으므로, 만약 문자열 마지막에 도달하면, 자동으로 마지막 수를 수 배열에 추가하게 한다

import sys
input = sys.stdin.readline

a = input().strip('\n')

num = list()
plusminus = list()
answer = ''
for i in range(len(a)):
    if a[i].isnumeric():
        answer += a[i]
    else:
        num.append(int(answer))
        plusminus.append(a[i])
        answer=''
    if i == len(a)-1:
        num.append(int(answer))
        answer = ''
isminus = 0
for i in range(len(plusminus)):
    if plusminus[i] == '-':
        num[i+1] = num[i+1] * -1
        isminus = 1
    elif isminus == 1 and plusminus[i] == '+':
        num[i + 1] = num[i + 1] * -1
print(sum(num))
