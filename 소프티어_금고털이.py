# 그리디 문제 -> 남은 용량보다 해당 금속의 남은 무게가 많다면, 남은 용량만큼 금속을 담고, 반복문 종료
# 아니라면, 남은 금속량 전부 담는다.
# 2차원 배열의 1번 인덱스로 정렬해야 하기에 key는 lambda를 사용하여 x를 1번째 인덱스로 설정한다. 앞에 x는 매개변수, x가 들어오면, 뒤에 정의한 식대로 반환한다.

import sys
input = sys.stdin.readline

backpack, num = map(int,input().split())
numnum = list()
for _ in range(num):
    numnum.append(list(map(int,input().split())))

numnum.sort(reverse=True,key=lambda x:x[1])
answer = 0

for i in numnum:
    if backpack < i[0]:
        answer += backpack * i[1]
        break
    else:
        answer += i[0] * i[1]
        backpack -= i[0]

print(answer)
