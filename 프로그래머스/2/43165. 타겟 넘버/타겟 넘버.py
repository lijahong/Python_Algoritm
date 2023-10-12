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


    
    