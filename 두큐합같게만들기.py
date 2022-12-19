#2022 카카오 테크 인턴쉽 코테 문제 - 두 큐 합 같게 만들기
from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = -2
    count = 0
    suma = sum(queue1)
    sumb = sum(queue2)
    samenum = suma + sumb
    
    #정수로 안나뉘어지면 -1
    if samenum % 2 != 0:
        return -1
    
    #최대 시도 횟수 = 원상태로 돌아오는 것
    limitcount = len(queue1) * 3
    
    while True:
        # 최대 시도 횟수도 안되면 -1
        if count == limitcount:
            answer = -1
            break;
            
        if suma == sumb:
            answer = count
            break;
        # queue.pop(0) , queue.append() 가 한 쌍
        tmp = 0
        if suma > sumb:
            tmp = queue1.popleft()
            queue2.append(tmp)
            suma = suma - tmp
            sumb = sumb + tmp
        elif sumb > suma:
            tmp = queue2.popleft()
            queue1.append(tmp)
            suma = suma + tmp
            sumb = sumb - tmp
        count += 1
        
    return answer
