# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    sumhash = 0
    hashdict = {}
    for i in participant:
        hashdict[hash(i)] = i
        sumhash += hash(i)
    for j in completion:
        sumhash -= hash(j)
    answer = hashdict[sumhash]
    return answer

# Counter 쓴 방법
from collections import Counter
def solution(participant, completion):
    answer = ''
    a = Counter(participant) - Counter(completion)
    answer = list(a.keys())[0]
    return answer
