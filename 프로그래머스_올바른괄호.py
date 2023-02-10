# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 괄호가 다 닫혔는지 확인하는 문제
# ( 리스트를 만들어서 )가 나올 때, pop 하게 한다. 만약 올바른 괄호라면 반복문이 끝났을 때, 리스트가 비어있을 것이다.
# 만약, )가 더 많은 경우, 리스트가 비어있을 때, pop하면 에러가 나므로, 조건문을 통해 비어있다면 False를 리턴하게 한다.

def solution(s):
    answer = True
    left = list()
    for i in s:
        if i == '(':
            a = left.append(i)
        if i == ')':
            if left:
                a = left.pop()
            else:
                return False
    if left:
        return False
    return True
