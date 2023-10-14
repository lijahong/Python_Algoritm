def solution(numbers, target):
    answer = 0
    countn = len(numbers)
    def dfs(count, suma):
        if count == countn :
            if suma == target:
                nonlocal answer
                answer += 1
        else:
            dfs(count + 1, suma + numbers[count])
            dfs(count + 1, suma - numbers[count])     
    dfs(0,0) 
    return answer