# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 프로그래머스 2023 KAKAO BLIND RECRUITMENT LV.2 이모티콘 할인행사
# 백트래킹을 이용하여 이모티콘 할인율에 대한 경우의 수 탐색을 한다
# 할인률 배열의 길이와 이모티콘 배열의 길이가 같다면, 가격 계산 및 이모티콘 플러스 가입 인원 계산 함수를 실행한다
# 반환된 값 비교에서 이모티콘 플러스 가입 인원 비교를 우선시 한다. 만약 반환된 인원값이 최대 인원값보다 더 크다면, 최대 인원값과 최대 금액값을 업데이트한다. 반환된 인원값이 최대 인원값과 같다면, 금액값을 비교하여 업데이트한다
# 백트래킹 함수가 종료되면, 최대 이모티콘 플러스 가입 인원 수에 대한 최대 이모티콘 판매 금액 수가 변수에 저장되있다. 이를 answer 배열에 append 하면 된다

def solution(users, emoticons):
    answer = []
    sales = [10,20,30,40]
    maxmoney, maxpeople = 0,0
    currentsale = list()
    
    def backtrack(currentsale):
        nonlocal maxmoney
        nonlocal maxpeople
        
        if len(currentsale) == len(emoticons):
            a,b = setting(users,currentsale,emoticons)
            if a > maxpeople:
                maxpeople,maxmoney = a,b
            elif a == maxpeople:
                if b > maxmoney:
                    maxpeople,maxmoney = a,b
        else:
            for i in sales:
                currentsale.append(i)
                backtrack(currentsale)
                currentsale.pop()
                
    backtrack(currentsale)
    answer.append(maxpeople)
    answer.append(maxmoney)
    return answer
                
def setting(users,currentsale,emoticons):
    allmoney = 0
    allpeople = 0
    for i in users:
        moneycount = 0
        for j in range(len(currentsale)):
            if i[0] <= currentsale[j]:
                moneycount += (emoticons[j] * (100 - currentsale[j]))//100
                
        if moneycount < i[1]:
            allmoney += moneycount
        else:
            allpeople += 1
    return allpeople,allmoney
