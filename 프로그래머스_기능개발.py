# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 앞에 작업의 진행 시간 값이 뒤에 작업의 진행 시간 값보다 클 경우, 앞에 작업이 끝나야 뒤에 미리 끝난 기능들이 배포되므로 count를 증가시킨다.
# 이전 가장 오래 걸리는 작업보다 더 오래 걸리는 작업이 나올 경우, 이전에 끝난 기능들이 모두 배포되야 하므로, count 값을 배열에 넣어야 한다.
# 이때, 현재 기준이 되는 작업도 세야하므로 count를 0이 아닌 1로 설정한다. 그 이후에 가장 오래 걸리는 작업 시간 값을 현재 작업의 소요 시간으로 설정한다.

from collections import deque

def solution(progresses, speeds):
    answer = []
    remainlist = deque([])
    
    for a,b in zip(progresses,speeds):
        remain = (100 - a) // b
        # 만약, 남은 일과 처리속도가 딱 나눠지지 않는 경우, 하루 더 걸린다.
        if ((100 - a) % b ) > 0: 
            remain += 1
        remainlist.append(remain)
    maxa = remainlist[0]
    count = 0
    while remainlist:
        work = remainlist.popleft()
        if work <= maxa:
            count += 1
        else:
            answer.append(count)
            maxa = work
            count = 1
    # 마지막 요소 넣기, 반복문에서 현재 진행 시간 값이 이전 가장 큰 진행 시간 값보다 큰 경우에만 기능 개수 값을 넣게 했기에 마지막에 배포될 기능 개수 값은 넣어지지 않는다. 
    # 따라서 반복문 종료 후,  마지막에 배포될 기능 개수 값도 넣어야 한다.
    answer.append(count) 
    return answer
