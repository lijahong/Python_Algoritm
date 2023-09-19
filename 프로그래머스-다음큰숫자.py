# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# counter랑 format 씀
from collections import Counter
def solution(n):
    answer = 0
    a = format(n,'b') # format(수,바꿀 진수 표기) = 문자열로 이진수 바꿔줌 , bin(수)[2:] 해도 같음
    acount = countit(a)
    while True:
        n += 1
        b = format(n,'b')
        if acount == countit(b):
            answer = n
            break
    
    return answer

def countit(n): # 걍 count('1') 해도 됨. 내장 함수라
    counter = Counter(n) # counter 객체 만듬, 딕셔너리 형태
    return counter['1'] # 키값 이용해서 벨류 출력
