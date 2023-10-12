# 문자열에서 가장 긴 A의 모임을 찾아서
# 1. 정주행
# 2. 0에서 A의 왼쪽 + A의 왼쪽에서 다시 0 + 맨끝에서 A의 오른쪽
# 3. 맨끝에서 A의 오른쪽(역방향으로) + A의 오른쪽에서 맨끝 + 0에서 A의 왼쪽
# 이 3개 비교하면 됨
# 이럴려면 현재 문자열에서 가장 긴 A의 모임을 찾아야하는데, 결국 문자열을 한번 돌아야함
# 그래서 반복문 하나로 같이 진행

def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i_index,i in enumerate(name):
        answer += min( ord(i) - 65, 90 - ord(i) + 1)
        next = i_index + 1 # 현재 수의 다음 포인터
        while next < len(name) and name[next] == 'A':
            next += 1 # 제일 긴 A 모임의 왼쪽은 i_index, 오른쪽은 next
        min_move = min(min_move , 2 * i_index + len(name) - next  , i_index + 2 * ( len(name) - next ))
        # 전체 길이에서 오른쪽 끝 포인터를 빼면, 좌측 끝에서 우측 끝으로 역이동하는 횟수도 포함된다
    answer += min_move         
    return answer
