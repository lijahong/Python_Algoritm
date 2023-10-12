# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3#
def solution(nums):
    answer = 0
    set1 = set(nums)
    answer = len(set1) if len(set1) < (len(nums) // 2) else len(nums) // 2
        
    return answer
