# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
# 문자열 분해 -> 순열 조합 -> 각 순열을 정수로 바꿈 -> 가장 큰 수를 기준으로 소수 리스트 생성 -> 문자열을 통해 만든 수가 소수 리스트에 있으면 answer 증가
# 좋은 방법은 아닌거 같다

from itertools import permutations
def solution(numbers):
    answer = 0
    numlist = list()
    
    for i in numbers:
        numlist.append(i)
        
    numlist2 = list()
    
    for i in range(1,len(numbers)+1):
        for j in permutations(numlist,i):
            numstr = ''
            for z in j:
                numstr += z
                if int(numstr) not in numlist2:
                    numlist2.append(int(numstr))
    sosulist = alesto(max(numlist2))
    for i in numlist2:
        if i in sosulist:
            answer += 1
    return answer

def alesto(numbers):
    sosulist = list()
    sosuright = [False,False] + [True] * ( numbers - 1 )
    
    for i in range(2,numbers+1):
        if sosuright[i] == True:
            sosulist.append(i)
            for j in range(i,numbers + 1, i):
                sosuright[j] = False
    return sosulist
