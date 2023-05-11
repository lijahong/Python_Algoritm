# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# 각 수가 + or - 일 가능성을 모두 봐야한다. 따라서 해당 문제는 하나의 트리 구조와 같다. 트리에서 깊게 탐색해야 하므로 dfs를 사용하였다

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(num,sumx):
        if num == n:
            if sumx == target:
                nonlocal answer
                answer += 1
        else:
            dfs(num+1,sumx + numbers[num])
            dfs(num+1,sumx - numbers[num])
    dfs(0,0)
    return answer
